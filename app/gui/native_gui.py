import html
import math
import re
import sys
from datetime import datetime
from urllib.parse import quote, unquote

from PyQt6.QtCore import QProcess, Qt, QTimer, QUrl
from PyQt6.QtGui import QBrush, QColor, QDesktopServices, QPainter, QPen, QTextCursor
from PyQt6.QtWidgets import (
    QApplication, QComboBox, QFileDialog, QFormLayout, QHBoxLayout, QLabel, QLineEdit,
    QGraphicsEllipseItem, QGraphicsScene, QGraphicsSimpleTextItem, QGraphicsView,
    QListWidget, QMainWindow, QMessageBox, QPushButton, QSplitter, QTabWidget,
    QTextBrowser, QTextEdit, QVBoxLayout, QWidget,
)

from app.core.config import ASSETS_PATH, ROOT_DIR, VAULT_PATH
from app.core.ink_engine import InkCanvas
from app.core.sandbox_manager import SandboxManager
from app.core.search_engine import SearchEngine
from app.core.study_tools import StudyTools
from app.core.wiki_manager import WikiManager
from ingestion.clipper import WebClipper
from ingestion.ingestor import Ingestor


class GraphNode(QGraphicsEllipseItem):
    def __init__(self, topic, color, open_note):
        super().__init__(-18, -18, 36, 36)
        self.topic = topic
        self.open_note = open_note
        self.setBrush(QBrush(QColor(color)))
        self.setPen(QPen(QColor("#c9d1d9"), 1))
        self.setToolTip(f"Double-click to open {topic}")
        self.setAcceptHoverEvents(True)

    def mouseDoubleClickEvent(self, event):
        self.open_note(self.topic)
        event.accept()


class GraphCanvas(QGraphicsView):
    COLORS = {"read": "#50fa7b", "reading": "#f1fa8c", "pending": "#ff5555", "unread": "#ff5555", "ghost": "#444444"}

    def __init__(self, open_note):
        super().__init__()
        self.open_note = open_note
        self.setScene(QGraphicsScene(self))
        self.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)
        self.setBackgroundBrush(QBrush(QColor("#0d1117")))

    def draw_graph(self, graph, wiki, empty_message="No linked notes yet.", focus=None):
        self.scene().clear()
        nodes = list(graph.nodes())
        radius = max(130, min(500, len(nodes) * 28))
        
        # If focusing on a single isolated node, we might want to show the message instead or in addition.
        # But here we'll show the message ONLY if the graph is truly empty OR if it only contains the focus node but with no neighbors.
        is_isolated_focus = focus and len(nodes) == 1 and focus in nodes and graph.number_of_edges() == 0
        
        if not nodes or is_isolated_focus:
            label = self.scene().addSimpleText(empty_message)
            label.setBrush(QBrush(QColor("#8b949e")))
            if is_isolated_focus:
                label.setPos(-label.boundingRect().width() / 2, -radius - 40)
            else:
                return

        positions = {}
        
        # Position focus node at center if provided
        other_nodes = [n for n in nodes if n != focus]
        if focus in nodes:
            positions[focus] = (0, 0)
        
        for index, topic in enumerate(other_nodes):
            angle = 2 * math.pi * index / max(len(other_nodes), 1)
            positions[topic] = (radius * math.cos(angle), radius * math.sin(angle))
            
        edge_pen = QPen(QColor("#48576a"), 1.5)
        for source, destination, data in graph.edges(data=True):
            x1, y1 = positions[source]
            x2, y2 = positions[destination]
            if source == destination:
                # Draw a self-loop (a circle next to the node)
                from PyQt6.QtCore import QRectF
                loop_rect = QRectF(x1 + 10, y1 - 30, 25, 25)
                self.scene().addEllipse(loop_rect, edge_pen)
            else:
                self.scene().addLine(x1, y1, x2, y2, edge_pen)
                
            # Draw label if present
            label = data.get("label", "")
            etype = data.get("type", "")
            if label or etype:
                text = f"{label} ({etype})" if etype else label
                label_item = QGraphicsSimpleTextItem(text)
                label_item.setBrush(QBrush(QColor("#8b949e")))
                label_item.setPos((x1 + x2) / 2, (y1 + y2) / 2)
                self.scene().addItem(label_item)
        for topic in nodes:
            x, y = positions[topic]
            is_ghost = graph.nodes[topic].get("ghost", False)
            color = self.COLORS["ghost"] if is_ghost else self.COLORS.get(wiki.get_status(topic), "#8b949e")
            node = GraphNode(topic, color, self.open_note)
            node.setPos(x, y)
            self.scene().addItem(node)
            label = QGraphicsSimpleTextItem(topic)
            label.setBrush(QBrush(QColor("#c9d1d9")))
            label.setPos(x + 23, y - 10)
            self.scene().addItem(label)
        bounds = self.scene().itemsBoundingRect().adjusted(-40, -40, 40, 40)
        self.scene().setSceneRect(bounds)
        self.fitInView(bounds, Qt.AspectRatioMode.KeepAspectRatio)

    def wheelEvent(self, event):
        factor = 1.2 if event.angleDelta().y() > 0 else 1 / 1.2
        self.scale(factor, factor)


class WikiStudyOS(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Wiki-Study OS")
        self.resize(1320, 840)
        self.wiki = WikiManager(VAULT_PATH)
        self.ingestor = Ingestor(VAULT_PATH)
        self.search = SearchEngine(VAULT_PATH)
        self.clipper = WebClipper(VAULT_PATH)
        self.study = StudyTools(VAULT_PATH)
        self.sandbox = SandboxManager(VAULT_PATH)
        self.current_topic = None
        self.web_results = []
        self.autosave = QTimer(self)
        self.autosave.setSingleShot(True)
        self.autosave.timeout.connect(self.save_note)
        self._build_ui()
        self.refresh_pages()
        self.refresh_dashboard()
        self.refresh_global_graph()
        self.refresh_local_graph()

    def _build_ui(self):
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
        self.tabs.addTab(self._dashboard(), "Dashboard")
        self.tabs.addTab(self._explorer(), "Explorer")
        self.tabs.addTab(self._search(), "Search")
        self.tabs.addTab(self._research(), "Research")
        self.tabs.addTab(self._graph(), "Graph")
        self.tabs.addTab(self._workspace(), "Workspace")
        self.tabs.addTab(self._lab(), "Lab Notebook")
        self.tabs.addTab(self._terminal(), "Terminal")
        self.tabs.addTab(self._settings(), "Settings")
        self.tabs.currentChanged.connect(self._on_tab_changed)
        self.setStyleSheet("""
            QMainWindow, QWidget { background:#0d1117; color:#c9d1d9; font-size:13px; }
            QTextEdit, QTextBrowser, QListWidget, QLineEdit, QComboBox { background:#161b22; color:#c9d1d9; border:1px solid #30363d; padding:5px; }
            QPushButton { background:#238636; color:white; border:0; border-radius:4px; padding:7px 12px; }
            QPushButton:hover { background:#2ea043; } QTabBar::tab { padding:9px 13px; }
        """)

    def _on_tab_changed(self, index):
        if index == 4: # Graph tab
            self.refresh_global_graph()
            self.refresh_local_graph()

    def _dashboard(self):
        page, layout = QWidget(), QVBoxLayout()
        page.setLayout(layout)
        layout.addWidget(QLabel("<h1>Wiki-Study OS</h1><p>Your local-first study vault.</p>"))
        self.stats = QLabel()
        layout.addWidget(self.stats)
        row = QHBoxLayout()
        for label, action in (("Import Files", self.import_files), ("Clip URL", self.prompt_clip), ("Rebuild Keyword Index", self.rebuild_index), ("Build Semantic Index", self.rebuild_semantic_index)):
            button = QPushButton(label); button.clicked.connect(action); row.addWidget(button)
        layout.addLayout(row); layout.addStretch()
        return page

    def _explorer(self):
        page, layout = QWidget(), QVBoxLayout(); page.setLayout(layout)
        toolbar = QHBoxLayout()
        for label, action in (("New", self.new_note), ("Save", self.save_note), ("Delete", self.delete_note), ("Auto-link", self.auto_link)):
            button = QPushButton(label); button.clicked.connect(action); toolbar.addWidget(button)
        self.status = QComboBox(); self.status.addItems(["pending", "unread", "reading", "read"]); self.status.currentTextChanged.connect(self.set_status)
        toolbar.addWidget(QLabel("Status:")); toolbar.addWidget(self.status); layout.addLayout(toolbar)
        splitter = QSplitter()
        self.pages = QListWidget(); self.pages.itemClicked.connect(lambda item: self.open_note(item.text()))
        self.editor = QTextEdit(); self.editor.textChanged.connect(lambda: self.autosave.start(700))
        self.preview = QTextBrowser(); self.preview.anchorClicked.connect(self.open_link)
        splitter.addWidget(self.pages); splitter.addWidget(self.editor); splitter.addWidget(self.preview)
        splitter.setSizes([220, 570, 430]); layout.addWidget(splitter)
        return page

    def _search(self):
        page, layout = QWidget(), QVBoxLayout(); page.setLayout(layout)
        row = QHBoxLayout(); self.search_query = QLineEdit(); self.search_mode = QComboBox(); self.search_mode.addItems(["keyword", "hybrid", "semantic"])
        button = QPushButton("Search"); button.clicked.connect(self.run_search)
        row.addWidget(self.search_query); row.addWidget(self.search_mode); row.addWidget(button); layout.addLayout(row)
        self.search_results = QListWidget(); self.search_results.itemDoubleClicked.connect(lambda item: self.open_search_result(item))
        layout.addWidget(self.search_results); return page

    def _research(self):
        page, layout = QWidget(), QVBoxLayout(); page.setLayout(layout)
        row = QHBoxLayout(); self.research_query = QLineEdit(); button = QPushButton("Search Web"); button.clicked.connect(self.run_research)
        row.addWidget(self.research_query); row.addWidget(button); layout.addLayout(row)
        self.research_results = QListWidget(); layout.addWidget(self.research_results)
        add = QPushButton("Add Selected To Vault"); add.clicked.connect(self.add_research_result); layout.addWidget(add)
        return page

    def _graph(self):
        page, layout = QWidget(), QVBoxLayout(); page.setLayout(layout)
        layout.addWidget(QLabel("<h2>Knowledge Graph</h2><p>Double-click a node to open its note. Node colors follow study status.</p>"))
        row = QHBoxLayout()
        global_button = QPushButton("Refresh Global Graph"); global_button.clicked.connect(self.refresh_global_graph)
        local_button = QPushButton("Refresh Current Note Graph"); local_button.clicked.connect(self.refresh_local_graph)
        external_global = QPushButton("Open Global Graph In Browser"); external_global.clicked.connect(lambda: self.open_graph())
        external_local = QPushButton("Open Local Graph In Browser"); external_local.clicked.connect(lambda: self.open_graph(focus=self.current_topic))
        quick_link = QPushButton("Link Current Note To..."); quick_link.clicked.connect(self.quick_link)
        row.addWidget(global_button); row.addWidget(local_button); row.addWidget(external_global); row.addWidget(external_local); row.addWidget(quick_link); layout.addLayout(row)
        self.graph_tabs = QTabWidget()
        self.global_graph = self._graph_view()
        self.local_graph = self._graph_view()
        self.graph_tabs.addTab(self.global_graph, "Global Graph")
        self.graph_tabs.addTab(self.local_graph, "Local Graph")
        layout.addWidget(self.graph_tabs)
        return page

    def _workspace(self):
        page, layout = QWidget(), QVBoxLayout(); page.setLayout(layout)
        row = QHBoxLayout(); clear = QPushButton("Clear"); clear.clicked.connect(lambda: self.canvas.clear())
        save = QPushButton("Save Workspace Session"); save.clicked.connect(self.save_workspace)
        row.addWidget(clear); row.addWidget(save); row.addStretch(); layout.addLayout(row)
        self.canvas = InkCanvas(); layout.addWidget(self.canvas); return page

    def _lab(self):
        page, layout = QWidget(), QVBoxLayout(); page.setLayout(layout)
        layout.addWidget(QLabel("<h2>Lab Notebook</h2><p>Run Python fenced code blocks from the current note. State is retained between cells.</p>"))
        row = QHBoxLayout(); self.cell_index = QComboBox()
        refresh = QPushButton("Load Cells"); refresh.clicked.connect(self.refresh_cells)
        run = QPushButton("Run Cell"); run.clicked.connect(self.run_cell)
        run_all = QPushButton("Run All"); run_all.clicked.connect(self.run_all_cells)
        row.addWidget(self.cell_index); row.addWidget(refresh); row.addWidget(run); row.addWidget(run_all); layout.addLayout(row)
        self.lab_output = QTextEdit(); self.lab_output.setReadOnly(True); layout.addWidget(self.lab_output); return page

    def _settings(self):
        page, layout = QWidget(), QVBoxLayout(); page.setLayout(layout); form = QFormLayout()
        form.addRow("Vault", QLabel(str(VAULT_PATH))); form.addRow("Assets", QLabel(str(ASSETS_PATH))); form.addRow("Project", QLabel(str(ROOT_DIR)))
        layout.addLayout(form); layout.addStretch(); return page

    def _terminal(self):
        page, layout = QWidget(), QVBoxLayout(); page.setLayout(layout)
        layout.addWidget(QLabel("<h2>Terminal</h2><p>Persistent PowerShell session rooted at the Wiki-Study OS project.</p>"))
        self.terminal_output = QTextEdit(); self.terminal_output.setReadOnly(True)
        self.terminal_input = QLineEdit(); self.terminal_input.setPlaceholderText("Enter a PowerShell command and press Enter")
        self.terminal_input.returnPressed.connect(self.run_terminal_command)
        row = QHBoxLayout()
        run = QPushButton("Run"); run.clicked.connect(self.run_terminal_command)
        clear = QPushButton("Clear"); clear.clicked.connect(self.terminal_output.clear)
        restart = QPushButton("Restart Shell"); restart.clicked.connect(self.start_terminal)
        row.addWidget(run); row.addWidget(clear); row.addWidget(restart); row.addStretch()
        layout.addWidget(self.terminal_output); layout.addWidget(self.terminal_input); layout.addLayout(row)
        self.terminal_process = QProcess(self)
        self.terminal_process.setWorkingDirectory(str(ROOT_DIR))
        self.terminal_process.setProcessChannelMode(QProcess.ProcessChannelMode.MergedChannels)
        self.terminal_process.readyReadStandardOutput.connect(self.read_terminal_output)
        self.start_terminal()
        return page

    def _graph_view(self):
        return GraphCanvas(self.open_note)

    def refresh_pages(self):
        current = self.current_topic
        self.pages.clear(); self.pages.addItems(self.wiki.get_all_pages())
        if current:
            matches = self.pages.findItems(current, __import__("PyQt6").QtCore.Qt.MatchFlag.MatchExactly)
            if matches: self.pages.setCurrentItem(matches[0])

    def refresh_dashboard(self):
        stats = self.wiki.vault_stats()
        self.stats.setText(f"<h2>{stats['total_pages']} notes</h2><p>Read: {stats['read']} &nbsp; Reading: {stats['reading']} &nbsp; Pending: {stats['pending']} &nbsp; Unread: {stats['unread']}</p>")

    def open_note(self, topic):
        topic = unquote(topic).strip()
        resolved = next((page for page in self.wiki.get_all_pages() if page.casefold() == topic.casefold()), None)
        if not resolved:
            QMessageBox.warning(self, "Missing note", f"The linked note does not exist:\n{topic}")
            return
        topic = resolved
        if self.current_topic: self.save_note()
        self.current_topic = topic
        content = self.wiki.read_page(topic) or ""
        self.editor.blockSignals(True); self.editor.setPlainText(content); self.editor.blockSignals(False)
        self.status.blockSignals(True); self.status.setCurrentText(self.wiki.get_status(topic)); self.status.blockSignals(False)
        self.update_preview(); self.refresh_cells(); self.refresh_local_graph()
        if self.tabs.currentIndex() not in {1, 4, 6}:
            self.tabs.setCurrentIndex(1)

    def update_preview(self):
        text = html.escape(self.editor.toPlainText())
        text = re.sub(r"!\[\[([^\]]+)\]\]", lambda m: f'<img src="{(ASSETS_PATH / m.group(1)).as_uri()}" width="520">', text)
        text = re.sub(r"\[\[([^\]]+)\]\]", self._render_wiki_link, text)
        self.preview.setHtml("<pre style='white-space:pre-wrap'>" + text + "</pre>")

    def open_link(self, url):
        if url.scheme() == "wiki":
            topic = unquote(url.path().lstrip("/"))
            section = unquote(url.fragment())
            self.open_note(topic)
            if section:
                self.preview.scrollToAnchor(section)
                self.preview.moveCursor(QTextCursor.MoveOperation.Start)
                self.preview.find(section)
        else: QDesktopServices.openUrl(url)

    def _render_wiki_link(self, match):
        target = html.unescape(match.group(1))
        destination, _, label = target.partition("|")
        topic, separator, section = destination.partition("#")
        topic = topic.strip() or (self.current_topic or "")
        href = f"wiki://note/{quote(topic)}"
        if separator:
            href += f"#{quote(section.strip())}"
        return f'<a href="{href}">{html.escape(label.strip() or destination.strip())}</a>'

    def save_note(self):
        if self.current_topic:
            self.wiki.write_page(self.current_topic, self.editor.toPlainText()); self.update_preview(); self.refresh_dashboard()

    def new_note(self):
        title, ok = self._ask("New note", "Title:")
        if ok and title.strip(): self.open_note(self.wiki.create_page(title))

    def delete_note(self):
        if self.current_topic and QMessageBox.question(self, "Delete note", f"Delete {self.current_topic}?") == QMessageBox.StandardButton.Yes:
            self.wiki.delete_page(self.current_topic); self.current_topic = None; self.editor.clear(); self.preview.clear(); self.refresh_pages(); self.refresh_dashboard()

    def set_status(self, status):
        if self.current_topic: self.wiki.update_status(self.current_topic, status); self.open_note(self.current_topic)

    def auto_link(self):
        self.save_note(); self.wiki.auto_link_all(); self.refresh_pages()
        if self.current_topic: self.open_note(self.current_topic)

    def import_files(self):
        paths, _ = QFileDialog.getOpenFileNames(self, "Import study materials", "", "Study files (*.pdf *.docx *.pptx *.txt *.md *.rst *.png *.jpg *.jpeg *.bmp *.webp)")
        for path in paths:
            try: self.ingestor.ingest(path)
            except Exception as exc: QMessageBox.warning(self, "Import failed", f"{path}\n\n{exc}")
        self.refresh_pages(); self.refresh_dashboard()

    def prompt_clip(self):
        url, ok = self._ask("Clip URL", "Website, YouTube, GitHub, or GitLab URL:")
        if ok and url.strip(): self.clipper.clip(url.strip()); self.refresh_pages(); self.refresh_dashboard()

    def rebuild_index(self):
        count = self.search.build_index(semantic=False); QMessageBox.information(self, "Search index", f"Indexed {count} chunks for keyword search.")

    def rebuild_semantic_index(self):
        count = self.search.build_index(semantic=True); QMessageBox.information(self, "Search index", f"Indexed {count} chunks with available semantic embeddings.")

    def run_search(self):
        self.search_results.clear()
        for result in self.search.search_local(self.search_query.text(), mode=self.search_mode.currentText()):
            item = f"{result['source']} | score {result['score']:.3f}\n{result['text'][:260]}"
            self.search_results.addItem(item)

    def open_search_result(self, item):
        self.open_note(item.text().split(" | ", 1)[0])

    def run_research(self):
        self.research_results.clear(); self.web_results = self.search.search_web(self.research_query.text())
        for result in self.web_results: self.research_results.addItem(f"{result['title']}\n{result['href']}\n{result['body']}")

    def add_research_result(self):
        row = self.research_results.currentRow()
        if 0 <= row < len(self.web_results):
            self.clipper.clip(self.web_results[row]["href"]); self.refresh_pages(); self.refresh_dashboard()

    def open_graph(self, focus=None):
        path = self.wiki.generate_graph(focus=focus); QDesktopServices.openUrl(QUrl.fromLocalFile(path))

    def refresh_global_graph(self):
        self.global_graph.draw_graph(self.wiki.build_graph(), self.wiki)

    def refresh_local_graph(self):
        if not hasattr(self, "local_graph"):
            return
        graph = self.wiki.build_graph()
        if self.current_topic and self.current_topic in graph:
            nodes = {self.current_topic, *graph.predecessors(self.current_topic), *graph.successors(self.current_topic)}
            graph = graph.subgraph(nodes).copy()
            message = "This note has no nearby linked notes yet."
        else:
            graph = graph.subgraph([]).copy()
            message = "Open a note to see its local graph."
        self.local_graph.draw_graph(graph, self.wiki, message, focus=self.current_topic)

    def save_workspace(self):
        title = "Workspace Session " + datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        asset = ASSETS_PATH / f"{title}.png"; self.canvas.save(asset)
        self.wiki.write_page(title, f"# {title}\n\n#pending\n\n![[{asset.name}]]\n")
        self.refresh_pages(); self.refresh_dashboard(); self.open_note(title)

    def quick_link(self):
        if not self.current_topic:
            QMessageBox.warning(self, "No note open", "Open a note first to add a link.")
            return
        target, ok = self._ask("Quick Link", f"Link '{self.current_topic}' to:")
        if ok and target.strip():
            content = self.wiki.read_page(self.current_topic) or ""
            content = content.rstrip() + f"\n\n[[{target.strip()}]]\n"
            self.wiki.write_page(self.current_topic, content)
            self.open_note(self.current_topic)

    def refresh_cells(self):
        self.cell_index.clear()
        if self.current_topic:
            cells = self.sandbox.list_cells(self.current_topic)
            for cell in cells:
                # Add item with index as data and a shortened preview as text
                preview = cell["preview"].replace("\n", " ")[:40]
                self.cell_index.addItem(f"Cell {cell['index']}: {preview}", cell["index"])

    def run_cell(self):
        if self.current_topic and self.cell_index.currentIndex() >= 0:
            cell_data = self.cell_index.currentData()
            result = self.sandbox.run_cell(self.current_topic, cell_data)
            self.lab_output.append(f"--- Cell {cell_data} Output ---")
            self.lab_output.append(result.get("output", "") or "(no output)")

    def run_all_cells(self):
        if self.current_topic:
            self.lab_output.clear()
            for result in self.sandbox.run_all(self.current_topic): self.lab_output.append(result.get("output", "") or "(no output)")

    def start_terminal(self):
        if self.terminal_process.state() != QProcess.ProcessState.NotRunning:
            self.terminal_process.kill()
            self.terminal_process.waitForFinished(1000)
        self.terminal_output.append(f"PowerShell terminal: {ROOT_DIR}")
        self.terminal_process.start("powershell.exe", ["-NoLogo", "-NoExit", "-Command", "-"])

    def run_terminal_command(self):
        command = self.terminal_input.text().strip()
        if command and self.terminal_process.state() == QProcess.ProcessState.Running:
            self.terminal_output.append(f"> {command}")
            self.terminal_process.write((command + "\r\n").encode("utf-8"))
            self.terminal_input.clear()

    def read_terminal_output(self):
        output = bytes(self.terminal_process.readAllStandardOutput()).decode("utf-8", errors="replace")
        if output:
            self.terminal_output.moveCursor(QTextCursor.MoveOperation.End)
            self.terminal_output.insertPlainText(output)
            self.terminal_output.moveCursor(QTextCursor.MoveOperation.End)

    def closeEvent(self, event):
        if hasattr(self, "terminal_process") and self.terminal_process.state() != QProcess.ProcessState.NotRunning:
            self.terminal_process.kill()
            self.terminal_process.waitForFinished(1000)
        super().closeEvent(event)

    def _ask(self, title, label):
        from PyQt6.QtWidgets import QInputDialog
        return QInputDialog.getText(self, title, label)


def main():
    app = QApplication(sys.argv)
    window = WikiStudyOS()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
