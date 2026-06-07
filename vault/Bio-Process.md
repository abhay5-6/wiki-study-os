---
source: C:/Users/abhay/Desktop/books/Bio-Process.pdf
date: 2026-06-01 22:23:57
---

# Bio-Process

#pending
@@a/p/k
## 📖 Study Outline
  - [[#contents-lists-available-at-sciencedirect|Contents lists available at ScienceDirect]]
- [[#journal-of-process-control|Journal of Process Control]]
- [[#marta-catal-ao-a-b-jos-e-pinto-a-b|Marta Catal ˜ ao a , b , Jos ´ e Pinto a , b , *]]
  - [[#1-introduction|1. Introduction]]
  - [[#2-materials-and-methods|2. Materials and methods]]
  - [[#2-1-microbiome-evolution-sbr|2.1. Microbiome evolution SBR]]
  - [[#2-2-pha-production-bioreactor|2.2. PHA production bioreactor]]
  - [[#2-3-analytical-methods|2.3. Analytical methods]]
  - [[#2-4-physics-informed-neural-network-pinn-model|2.4. Physics Informed Neural Network (PINN) model]]
@@k/p/a
  - [[#wmse-data-1-m|WMSE data = 1 M]]
  - [[#the-physics-loss-is-then-given-as|The physics loss is then given as:]]
  - [[#wmse-physics-k|WMSE physics = ∑ K]]
  - [[#2-5-sbr-control-system|2.5. SBR control system]]
  - [[#c-k-1-ac-0-c-k-ac|C ( k + 1 ) Ac ( 0 ) = C ( k ) Ac]]
  - [[#c-k-1-n-0-c-k-n|C ( k + 1 ) N ( 0 ) = C ( k ) N]]
  - [[#2-6-implementation|2.6. Implementation]]
  - [[#3-results-and-discussion|3. Results and discussion]]
  - [[#3-1-historical-microbiome-data-set|3.1. Historical microbiome data set]]
  - [[#3-2-pinn-training-on-the-historical-data|3.2. PINN training on the historical data]]
  - [[#3-3-transfer-learning|3.3. Transfer learning]]
  - [[#3-4-process-control-experiment|3.4. Process control experiment]]
  - [[#3-5-pha-production-experiment|3.5. PHA production experiment]]
  - [[#4-conclusions|4. Conclusions]]
  - [[#credit-authorship-contribution-statement|CRediT authorship contribution statement]]
  - [[#declaration-of-competing-interest|Declaration of Competing Interest]]
  - [[#acknowledgements|Acknowledgements]]
  - [[#data-availability|Data availability]]
  - [[#data-will-be-made-available-on-request|Data will be made available on request.]]
  - [[#references|References]]

## 🎯 Active Study Goals
- [ ] Master the formulas
- [ ] Summarize main chapters
- [ ] Pass the quiz

---


--- Page 1 ---
""" python
pip install numpy
"""





| A R T I C L E I N F O               | A B S T R A C T                                                                                                     |
|:------------------------------------|:--------------------------------------------------------------------------------------------------------------------|
| Keywords:                           | Manypreviousstudieshaveinvestigatedtheeconomicproductionofpolyhydroxyalkanoates(PHA)bynatural                       |
| PhysicsInformedNeuralNetworks(PINN) | microbiomes. A key underlying strategy is the feast and famine (F/F) feeding regimen for bacteria selection. For    |
| Transferlearning                    | this purpose, a sequencing batch reactor (SBR) is commonly operated in a sequence of F/F cycles until an evolved    |
| Model-Predictive Control (MPC)      | microbiome is attained with high PHA storage capacity. The effectiveness of this process is critically dependent    |
| Polyhydroxyalkanoates(PHA)          | on control parameters such as the hydraulic retention time (HRT) , organic iloading rate (OLR) and carbon-to-       |
| Naturalmicrobiomes                  | nitrogen ratio (C/N) applied at each cycle. This study evaluates for the frst time a physics-informed neural        |
| SequencingBatchReactor(SBR)         |                                                                                                                     |
|                                     | network (PINN) for model predictive control (MPC) of microbiome evolution in a SBR . A PINN model was trained       |
|                                     | on historical data collected in a SBR operated over 93 days and 31 cycles. Carbon (acetate) , Nitrogen (ammo­       |
|                                     | nium) , Volatile Suspended Solids (VSS) and intracellular PHA concentration data were used to train and validate    |
|                                     | the PINN . Subsequently, a second SBR experiment was conducted under automatic control of the PINN over a           |
|                                     | period of 36 days and 12 cycles. A transfer learning method was implemented leverage on in-process data to          |
|                                     | minimize process-model mismatch . The results showed a systematic cycle-to-cycle prediction error decrease. The     |
|                                     | intracellular PHA con centration systematic increased from 0 .51 % (w/w) to 16 .5 % (w/w) at the 12th cycle (32-    |
|                                     | i                                                                                                                   |
|                                     | fold increase i) . The fnal evolved microbiome, collected at the 12th cycle, was inoculated in a production reactor |
|                                     | yielding a fnal intracellular PHA content of 52 .86 % (w/w) an id volumetric concentration of 8 .93 g PHA/L .       |
|                                     | Overall , the PINN-MPC meth i od has shown high potential to effciently explore the reactor design space and to     |
|                                     | implement in autonomy effcient strategies for natural microbiome evolution.                                         |


Journal of Process Control 156 (2025) 103594

## Contents lists available at ScienceDirect <a id="contents-lists-available-at-sciencedirect"></a>


![[Bio-Process_img_6d0acd79a9.jpeg]]


# Journal of Process Control <a id="journal-of-process-control"></a>

journal homepage: www.elsevier.com/locate/jprocont
Bioprocess model-predictive control with physics-informed neural networks: Driving microbiome evolution toward high polyhydroxyalkanoates production capacity

# Marta Catal ˜ ao a , b , Jos ´ e Pinto a , b , * <a id="marta-catal-ao-a-b-jos-e-pinto-a-b"></a>

, Cristiana A.V. Torres a , b , Filomena Freitas a , b , Maria A.M. Reis a , b , Rafael S. Costa a , b , Rui Oliveira a , b
a Associate Laboratory i4HB - Institute for Health and Bioeconomy, NOVA School of Science and Technology, Universidade NOVA de Lisboa, Caparica 2829-516, Portugal b UCIBIO - Applied Molecular Biosciences Unit, Department of Chemistry, NOVA School of Science and Technology, Universidade NOVA de Lisboa, Caparica 2829-516, Portugal
A R T I C L E I N F O
A B S T R A C T
Keywords: Physics Informed Neural Networks (PINN) Transfer learning Model-Predictive Control (MPC) Polyhydroxyalkanoates (PHA) Natural microbiomes Sequencing Batch Reactor (SBR)
Many previous studies have investigated the economic production of polyhydroxyalkanoates (PHA) by natural microbiomes. A key underlying strategy is the feast and famine (F/F) feeding regimen for bacteria selection. For this purpose, a sequencing batch reactor (SBR) is commonly operated in a sequence of F/F cycles until an evolved microbiome is attained with high PHA storage capacity. The effectiveness of this process is critically dependent on control parameters such as the hydraulic retention time (HRT), organic loading rate (OLR) and carbon-to- nitrogen ratio (C/N) applied at each cycle. This study evaluates for the first time a physics-informed neural network (PINN) for model predictive control (MPC) of microbiome evolution in a SBR. A PINN model was trained on historical data collected in a SBR operated over 93 days and 31 cycles. Carbon (acetate), Nitrogen (ammo­ nium), Volatile Suspended Solids (VSS) and intracellular PHA concentration data were used to train and validate the PINN. Subsequently, a second SBR experiment was conducted under automatic control of the PINN over a period of 36 days and 12 cycles. A transfer learning method was implemented leverage on in-process data to minimize process-model mismatch. The results showed a systematic cycle-to-cycle prediction error decrease. The intracellular PHA concentration systematic increased from 0.51 % (w/w) to 16.5 % (w/w) at the 12th cycle (32- fold increase). The final evolved microbiome, collected at the 12th cycle, was inoculated in a production reactor yielding a final intracellular PHA content of 52.86 % (w/w) and volumetric concentration of 8.93 g PHA/L. Overall, the PINN-MPC method has shown high potential to efficiently explore the reactor design space and to implement in autonomy efficient strategies for natural microbiome evolution.

## 1. Introduction <a id="1-introduction"></a>

Physics-Informed Neural Networks (PINNs) are a recent machine learning (ML) method that incorporates physical laws into the training process of neural networks [1] . They belong to the broader class of hybrid modelling approaches, which integrate mechanistic and data-driven models within a unified framework [2 – 4] . It was first pro­ posed to describe high-dimensional fluid dynamics problems (based on the Navier-Stokes equations or systems of partial differential equations in general) and has quickly evolved to applications in many other fields
* Corresponding author at: Associate Laboratory i4HB - Institute for Health and Bioeconomy, NOVA School of Science and Technology, Universidade NOVA de Lisboa, Caparica 2829-516, Portugal.
E-mail address: jmm.pinto@campus.fct.unl.pt (J. Pinto).
https://doi.org/10.1016/j.jprocont.2025.103594 Received 31 July 2025; Received in revised form 31 October 2025; Accepted 14 November 2025
Available online 21 November 2025 0959-1524/© 2025 The Authors. Published by Elsevier Ltd. This is an open access article under the CC BY-NC-ND license ( http://creativecommons.org/licenses/by- nc-nd/4.0/ ).
[1,5,6] . PINNs adopt Deep Neural Networks (DNN) to parameterize process state variables as function of time, spatial coordinates and external inputs. Automatic differentiation (AD) is used to calculate partial derivatives of the state variables in time and spatial coordinates. Training involves minimizing two types of residuals: (i) the difference between predicted and measured values of the state variables, and (ii) the residuals resulting from violations of the governing physical equa­ tions. This allows PINNs to learn from both experimental data and un­ derlying physics. Moreover, specialized DNN topologies can be designed to incorporate physical constraints, leading to more accurate and

![[Bio-Process_img_20167f4897.jpeg]]



--- Page 2 ---


M. Catal ˜ ao et al. Journal of Process Control 156 (2025) 103594
generalizable models. This is in contrast with conventional DNN models that typically allow for good fitting of a system, but their prediction may be inconsistent when performing extrapolation [7] . Furthermore, PINNs can be effectively trained on limited data, making them well-suited for scientific applications where large datasets are unavailable [8] . This capability positions PINNs as a promising framework across a wide range of scientific disciplines [9 – 12] .
The use of PINNs in bioprocess modelling and control is still in its early stages. Recently, Cui et al. [13] trained a PINN using physical laws (namely mass balances and kinetic rate laws) and bioreactor data to model the dynamics of fed-batch Chinese hamster ovary (CHO) cultures. Mowbray et al. [14] proposed a PINN with reinforcement learning (RL) for bioprocess kinetics identification. This approach correctly identified the underlying kinetic structures and showed high prediction accuracy (average error of 1.3 %). Rogers et al. [15] proposed a PINN to infer time-varying kinetic parameters from bioprocess data. Lagergren et al. [16] introduced a variant of PINNs, incorporating biological knowledge as physical constraints, and termed the approach biologically informed neural networks (BINNs). In this work, the physical constraints were based on governing reaction – diffusion partial differential equations, and the training data consisted of cell density measurements from multiple in vitro biological experiments. Yazdani et al. [17] proposed systems-biology-informed neural networks (SBINNs), where physical knowledge was derived from kinetic ordinary differential equations (ODE) encoded in the Systems Biology Markup Language (SBML). Dar­ yakenari et al. [18] proposed a framework termed AI-Aristotle that combines PINNs with symbolic regression (SR) for parameter discovery and gray-box identification. The results showed that PINNs can accu­ rately estimate model parameters using sparse data, and that symbolic regression (SR) can successfully identify missing terms in the governing ODEs.
Beyond cell culture process, PINNs are also being used to model chemical reactor processes. Asrav and Aydin [19] formulated PINNs with recurrent neural network (RNN) and termed it as physics-informed recurrent neural networks (PI-RNN). The authors also proposed physics- informed long-short term memory neural networks (PI-LSTM) and physics-informed gated recurrent unit (PI-GRU). The authors trained these PINNs using data from a semi-batch reactor (chemical reactions) and a wastewater treatment unit (biological, physicochemical and biochemical processes) and used physical knowledge of the ordinary differential equations (ODEs) governing the process dynamics to train the models. The authors concluded that PINNs have higher predictive power compared to the physics uninformed models in most scenarios. Similarly, Zheng et al. [20] used PI-RNNs to models a continuous chemical process and used known physical equations to train the model. The PI-RNN approach yielded the highest prediction accuracy and the best closed-loop control performance within a model-predictive control (MPC) experiment.
The present study addresses for the first time the development of a PINN for model-based control of PHA production by natural micro­ biomes. A microbiome comprises communities of microorganisms inhabiting a shared environment [21] . Within these environments, bacteria interact via mechanisms such as quorum sensing and metabolic cross-feeding, resulting in complex consortia. Microbiomes are note­ worthy to several biotechnological applications, including bioremedia­ tion of contaminated environments [22,23] , wastewater treatment [24] , biofuel production [25] and the production of biopolymers such as PHA [26] . PHAs are intracellular, biodegradable polymers accumulated by various microorganisms under conditions of nutrient limitation (typi­ cally ammonia or phosphate). Owing to their thermoplastic and elas­ tomeric properties, PHAs are regarded as promising biodegradable alternatives to petroleum-based plastics [27] . Among the different ap­ proaches for PHA production, the use of natural microbiomes has gained significant attention due to its operational flexibility and ability to uti­ lize low-cost, renewable carbon sources, including industrial and agri­ cultural waste streams [28 – 32] . Natural microbiomes can be selectively
enriched in a SBR to favor PHA-accumulating populations by applying operational strategies that impose periodic nutrient limitation and external substrate excess, such as F/F regimes [33,34] . This approach confers a competitive advantage to bacteria capable of assimilating carbon substrates and storing them intracellularly as PHA during the feast phase, followed by their utilization for growth and maintenance during the famine phase. As a result, bacteria unable to synthesize PHA reserves are progressively removed from the system [35,36] . SBR con­ trol parameters such as the HRT, OLR and C/N applied at each F/F cycle play a key role in the selection process. This study investigates a PINN framework to control these parameters. Two fundamental objectives guided this study. The first was the need to create a flexible modelling framework of microbiome dynamics that is not data intensive, due to the difficulty in acquiring large amounts of high-quality data, and that learns through experience, with the capability to evolve along with the microbiome. The second objective was to apply the dynamic modelling framework to optimize the F/F cycles of a SBR to efficiently control the microbiome evolution toward high PHA storage capacity.

## 2. Materials and methods <a id="2-materials-and-methods"></a>


## 2.1. Microbiome evolution SBR <a id="2-1-microbiome-evolution-sbr"></a>

The initial unevolved microbial consortium was obtained from sed­ iments collected in a salt marsh of the Tagus River estuary, in Corroios, Portugal (38.640805, − 9.129458). The initial microbiome ’ s genetic characterization was conducted by DNASense ’ s [37] custom workflow that targets variable regions of the 16S rRNA gene (V1 – V8 for bacteria) for amplicon sequencing. The obtained results are then bio­ informatically compared against taxonomic databases such Green­ genes2 2022.10 [38] , SILVA 138.2 99 % NR [39] and MiDAS 5.3 [40] . The results show a dominance of families Corynebacteriaceae (44.3 %), Microbactericeae (11.2 %), Paracoccaceae (7.3 %) and Pseudomona­ daceae (11.9 %). In order to enrich this microbiome in PHA accumu­ lating organisms, a F/F selection strategy was applied in a SBR with a working volume of 2.00 L. The SBR was initially inoculated with sludge of the initial unevolved microbial consortium (30 % volume of reactor) and operated under sterile conditions. The temperature and [[pH]] were kept at 20.00 ± 0.50 º C and 8.00 ± 0.10 respectively. The reactor was operated at a constant aeration rate of 1 vol of air per volume of medium per minute (vvm) and a constant agitation of 300 rotations per minute (rpm). The mineral cultivation medium was composed of (per liter): CaCl 2 , 0.07 g; EDTA, 0.10 g; MgSO 4 , 0.60 g; KH 2 PO 4 , 0.45 g; K 2 HPO 4 , 0.92 g; Mineral solution, 1 mL. The mineral solution composition was as follows (per liter): FeCl 3 ⋅ 6 H 2 O, 0.20 g; H 3 BO 4 , 0.32 g; CuSO 4 ⋅ 5 H 2 O, 0.06 g: Kl, 0.06 g; MnCl 2 ⋅ 4 H 2 O, 0.26 g; Na 2 MoO 4 ⋅ 2 H 2 O, 0.13 g; ZnSO 4 ⋅ 7 H 2 O, 0.26 g and CoCl 2 ⋅ 6 H 2 O, 0.32 g.
Two SBR experiments were conducted under the conditions above. The first SBR experiment served to collect historical data to train the PINN. Each F/F cycle had a fixed duration of 72 h (3 days). The reactor was operated for 93 days corresponding to 31 cycles. At the end of each cycle a volume of well mixed suspension was rapidly purged by a peri­ staltic pump (~5 min). Immediately after, 3 different solutions were fed simultaneously by 3 different peristaltic pumps marking the onset of a new F/F cycle. The acetate solution consisted of the basal mineral me­ dium complemented with 6.83 g/L of anhydrous sodium acetate. The ammonium solution consisted of the basal mineral medium com­ plemented with 1.60 g/L of NH 4 Cl. The fresh medium solution had the same composition of the mineral basal medium. The total volume of the 3 feed solutions was always the same as the purge volume, thus the working volume was kept constant throughout the process. The SBR was operated under a constant HRT of 30 days. This implied a volume of purge at each cycle of 200 mL. The OLR was kept constant to 1.67 g/ (L day) of acetate. The C/N ratio was 11.36 g/g until 2xHRT (60 days) and it was afterwards adjusted to 22.73 until the end of process to avoid ammonia accumulation.
2


--- Page 3 ---


M. Catal ˜ ao et al. Journal of Process Control 156 (2025) 103594
The second SBR experiment was operated under automatic control of the PINN. It started with an unevolved microbiome collected from the same site as the first SBR experiment. The duration of F/F cycles was also 72 h (3 days) and it was operated for 36 days corresponding to 12 F/F cycles. The purge and feed events were automatically controlled by digital timers connected to three peristaltic pumps. The volume of purge and feed solutions at each F/F cycle were automatically controlled by the PINN based controller as described below. This resulted in cycle-to- cycle variations of HRT, OLR and C/N ratio. The system was configured with a maximum purge volume of 400 mL to avoid washout and un­ stable operation. All other conditions were kept the same as in the first SBR experiment.

## 2.2. PHA production bioreactor <a id="2-2-pha-production-bioreactor"></a>

A second bioreactor operated in fed-batch mode was inoculated with the biomass purged from the selection SBR. It was fed with multiple pulses of acetate to assess the microbiome ’ s maximum PHA storage capacity. This assay was conducted in a 2.00 L bioreactor (BioStat B- Plus, Sartorius, Germany) with a 1.50 L working volume. The temper­ ature and [[pH]] were kept at 20.00 ± 0.50 º C and 8.00 ± 0.10 respectively. The mineral cultivation medium was the same as in the selection stage (described above). The reactor was inoculated with a 500 mL purge of the selection SBR collected at the end of the famine phase. The PHA accumulation assay was carried out using a multiple pulse-feed strategy controlled by the dissolved oxygen (DO) concentration. The end of each pulse was marked by a sudden increase in DO, signaling the exhaustion of the carbon source and triggering the feeding events of the following pulse. Ammonia was added only in the first pulse to promote some initial biomass growth, followed by an ammonia limitation strategy to maxi­ mize PHA production (pulses with carbon source only). Aeration was controlled at 1 vvm, while agitation was maintained at 300 rpm. The [[pH]] was regulated at 8.00 ± 0.05 through automatic dosing of 2 M HCl and 2 M NaOH.

## 2.3. Analytical methods <a id="2-3-analytical-methods"></a>

Volatile suspended solids (VSS) and total suspended solids (TSS) were determined as described in standard methods [32] . Carbon source (acetate) was quantified by high performance liquid chromatography (HPLC) using a VWR Hitachi Chromaster, as described by Matos et al. [41] . Five acetic acid standards with concentrations of 0.12, 0.25, 0.50, 0.75 and 1.00 g/L were prepared. Ammonia concentrations were determined through a colorimetric method with a segmented flow analyzer (Skalar San ++ , Skalar Analytical, the Netherlands). Standards with concentrations between 0.20 and 20.00 mg/L were prepared. Cell pellets after centrifugation (13,131 × g , 15 min, at 4 ◦ C) were washed with 5 mL of deionized water and freeze-dried overnight. Gas chroma­ tography (GC) was performed with flame ionization detector (FID) to determine the concentration of PHA as described by Pereira et al. [42] . Briefly, lyophilized samples were hydrolyzed in 1 mL of methanol acidic (20 %, v/v) sulfuric acid (SIGMA-ALDRICH) in methanol (Fisher Chemical) and 1 mL of benzoic acid in chloroform (1 g/L) (SIGMA-AL­ DRICH), on an oil bath at 100 ˚ C, for 4 h. Then, 1 mL of deionized water was added. After phase separation, the organic phase, with the resulting methyl esters, was transferred to vials and analyzed by GC (430-GC, Bruker) with a Restek column of 60 m, 0.53 mmID, 1 μ M df, Crossbond, Stabilwax. The injection volume was 2.0 μ L, with a running time of 32 min, a constant pressure of 14.50 psi and helium as carrier gas. The heating ramp was: 0 – 3 min, a rate of 20 ˚ C/min, until 100 ˚ C; 3 – 21 min, a rate of 3 ˚ C/min, until 155 ˚ C; and 21 – 32 min, a rate of 20 ˚ C/min, until 220 ̊ C. Hydroxybutyrate (HB) and hydroxyvalerate (HV) concentrations were determined through the use of two calibration curves, one for HB and other for HV, using standards (0.1 – 10 g/L) of a commercial co-polymer P(HB-HV) (88 %-12 %) (Sigma), and corrected using hep­ tadecane as internal standard (concentration of approximately 0.5 g/L).

## 2.4. Physics Informed Neural Network (PINN) model <a id="2-4-physics-informed-neural-network-pinn-model"></a>

The PINN model developed in this study is represented in Fig. 1 . Its ’ backbone is a single deep FFNN with 5 input nodes ( t and initial cycle conditions), multiple hidden layers (optimized), and 8 output nodes (4 state variables and 4 kinetic rates). The PINN predicts 4 state variables, namely active biomass concentration ( X a , g/L), acetate concentration in the liquid ( C Ac , g/L), ammonium concentration in the liquid ( C N , g/L), and intracellular PHA concentration ( f PHA , g/gVSS). The PINN also predicts 4 kinetic rates, namely the specific growth rate ( μ , h − 1 ), the specific acetate consumption rate ( v Ac , g/gh), the specific ammonium consumption rate ( v N , g/gh) and the specific PHA production rate ( v PHA , g/gh). The PINN inputs were cultivation time, t , and initial concentra­ tions at the beginning of the cycle ( X a ( 0 ) , C Ac ( 0 ) , C N ( 0 ) , f PHA (0))The PINN training simultaneously minimized an experimental data loss function and a physics loss function. The experimental data loss function was the weighted mean squared error between measured ( C ∗ j , i ) and
predicted ( C j , i ) concentrations over i = 1 , … , M measured points:
( C ∗ j , i − C j , i
) 2
∑ M

## WMSE data = 1 M <a id="wmse-data-1-m"></a>

∑
, C j = X a , C Ac , C N , f PHA (1)
σ Cj
i = 1
j
where σ Cj is the standard deviation of measured concentrations ( C ∗ j , i ) over i = 1 , … , M measured points. The physics loss function is based on material balance equations in a perfectly mixed batch bioreactor expressed by ordinary differential equations (ODEs):
dX a
dt − μ X a = e ode , 1 (2a)
dC Ac
dt + v Ac X a = e ode , 2 (2b)
dC N
dt + v N X a = e ode , 3 (2c)
df PHA
dt − v PHA + μ f PHA = e ode , 4 (2d)

## The physics loss is then given as: <a id="the-physics-loss-is-then-given-as"></a>

( e ode , k , j
) 2

## WMSE physics = ∑ K <a id="wmse-physics-k"></a>

∑ 4
σ ode , l
i = 1
k = 1
with K the number of colocation points, e ode , k , j physics residuals and σ ode , l the standard deviation of physics residuals.
Finally, the overall loss, loss , is a weighted sum of the data and physics loss terms:
loss = ( 1 − λ ) WMSE data + λ WMSE physics (4)
The choice of hyperparameter λ , which sets the relative importance of the physics and data loss terms, was optimized as it significantly impacts on the training and validation of the PINN. Automatic Differ­ entiation (AD) was applied to compute the gradients of the loss function in relation to the PINN parameters. AD was also applied to estimate the derivatives in Eq. (2a-d) . The python package Torch was used for AD. Throughout the study, we used the adaptive moment estimation (ADAM) algorithm, the tanh activation function, three hidden layers with 25 nodes each (pre-optimized), and 2000 epochs to train the PINN.

## 2.5. SBR control system <a id="2-5-sbr-control-system"></a>

A MPC system was implemented in python and integrated in the SBR bioreactor to automatically control the operation ( Fig. 2 ). The core of the control system is the PINN model that forecasts SBR dynamics as function of control degrees of freedom. The PINN was initially trained on historical data of 31 F/F cycles and then transferred to the control sys­ tem. Additionally, a transfer learning scheme was implemented based on
3
(3)


--- Page 4 ---


M. Catal ˜ ao et al. Journal of Process Control 156 (2025) 103594

![[Bio-Process_img_5c5d6dd36c.jpeg]]

Fig. 1. PINN structure describing microbiome growth and PHA accumulation in the sequencing batch reactor. The PINN contains two different losses: (1) The data loss, defined as the difference between measured data and predicted values, and (2) the physics loss, defined as the error resulting from a mismatch on physical constraints.

![[Bio-Process_img_b7eb7ba107.jpeg]]

Fig. 2. Schematic representation of the PINN based MPC of natural microbiome evolution in the SBR. The PINN model is trained on historical data (Off-line learning) and in-process data (Transfer learning). The control parameters (HRT, OLR and NLR) are optimized in the transition between F/F cycles. The PINN is set to forecast the effect of control parameters in the microbiome evolution 20 cycles in the future. A PINN-based central composite design (CCD) heuristic determines the HRT, OLR and NLR to be applied in the following F/F cycle.
4


--- Page 5 ---


M. Catal ˜ ao et al. Journal of Process Control 156 (2025) 103594
measured data of the running process to minimize plant-model mismatch (more to this in the results section). Due to their fast simu­ lation capabilities, PINNs can serve as surrogates for complex dynamical systems, enabling effective nonlinear closed-loop control. Indeed, PINNs have demonstrated excellent closed-loop performance within a MPC framework [42] . In the present problem, control actions are determined every three days thus CPU was not a limiting factor. Consequently, the control parameters for each F/F cycle were optimized based on the PINN dynamic forecast 20 F/F cycles in the future and a simple Central Composite Design (CCD) heuristic. At the end of cycle, k , the specific
OLR ( k + 1 ) (g/gVSSd), specific NLR ( k + 1 ) (g/gVSSd) and HRT ( k + 1 ) (d) are optimized for cycle k + 1. For this purpose, a CCD with 3 factors ( OLR , NLR , HRT ) and 5 levels (-1.6818, − 1, 0, 1, 1.6818) was applied, yielding 15 experiments without repetitions. The CCD center point at cycle k + 1 was the set as the operational point applied at the past cycle k. For each CCD experiment, the PINN takes as inputs the initial conditions specified by the design:
) (5a)
X ( k + 1 ) a ( 0 ) = X ( k ) a ( t cycle ) ( 1 − t cycle HRT ( k + 1 )
) ( 1 − t cycle HRT ( k + 1 )
) + OLR ( k + 1 ) t cycle X ( k + 1 ) a ( 0 ) (5b)
( t cycle

## C ( k + 1 ) Ac ( 0 ) = C ( k ) Ac <a id="c-k-1-ac-0-c-k-ac"></a>

) ( 1 − t cycle HRT ( k + 1 )
) + NLR ( k + 1 ) t cycle X ( k + 1 ) a ( 0 ) (5c)
( t cycle

## C ( k + 1 ) N ( 0 ) = C ( k ) N <a id="c-k-1-n-0-c-k-n"></a>

f ( k + 1 ) PHA ( 0 ) = f ( k ) PHA ( t cycle ) (5d)
As next step, the PINN is set to forecast the process dynamics 20 cycles in the future (from k + 1 to k + 20). The profit function is calculated as the volumetric PHA concentration at cycle k + 20 at the end of the feast phase ( t feast ) :
( t feast
) f ( k + 20 ) PHA ( t feast ) (6)
profit ( k + 20 ) = X ( k + 20 ) a
The optimal parameters ( OLR ( k + 1 ) , NLR ( k + 1 ) , HRT ( k + 1 ) ) to apply in the following cycle ( k + 1) are then taken from the response surface with
highest profit ( k + 20 ) value. The optimal control parameters are translated into the volume of purge, V ( k + 1 ) purge , and the volume of 3 feed solutions
(volume of acetate solution, V ( k + 1 ) Ac , the volume of ammonia solution,
V ( k + 1 ) N , and the volume fresh medium, V ( k + 1 ) mediumn ) at the beginning of cycle k + 1, according to the following equations:
V ( k + 1 ) Ac = OLR ( k + 1 ) X ( k + 1 ) a ( 0 ) t cycle V C Ac , feed
V ( k + 1 ) N = NLR ( k + 1 ) X ( k + 1 ) a ( 0 ) t cycle V C N , feed
V ( k + 1 ) medium = max ( 0 , V t cycle HRT ( k + 1 ) − V ( k + 1 ) Ac − V ( k + 1 ) N ) (7c)
V ( k + 1 ) purge = V ( k + 1 ) Ac + V ( k + 1 ) N + V ( k + 1 ) medium ≤ 400 mL (7d)
As may be noted in Eq. (7a-d) , the feeding volumes at each cycle depend on the PINN prediction of active biomass at the end of the previous cycle, since these variables were not available online in the physical bioreactor setting. For comparability reasons the duration of cycles, t cycle , was set constant to 3 days. Furthermore, the HTR was constrained to ≥ 15 days, corresponding to a maximum volume of purge of 400 mL, to avoid large perturbations in the reactor.

## 2.6. Implementation <a id="2-6-implementation"></a>

All methods were implemented in Python version 3.12.12. The PINN model training and transfer learning used packages pandas, torch,
numpy, sklearn and matplotlib. The SBR control was section was also implemented in Python using packages pandas, torch, numpy and sklearn. PINN training, transfer learning and control calculations were performed off-line. Control actions to the peristaltic pumps were set manually by adjusting pumping time at the beginning of each new SBR cycle.

## 3. Results and discussion <a id="3-results-and-discussion"></a>


## 3.1. Historical microbiome data set <a id="3-1-historical-microbiome-data-set"></a>

The initial unevolved microbiome underwent a SBR cultivation experiment for 93 days by applying the previously described F/F se­ lection protocol. This experiment corresponded to 3xHRTs and 30xF/F cycles. Fig. 3 shows the cultivation dynamics in terms of VSS (green) and intracellular PHA content (red) over the 30xF/F cycles. Intracellular PHA accumulation occurs during the feast phase, when acetate is in great excess, corresponding to approximately the first 12 h of each cycle. The famine phase starts upon acetate depletion and lasts for approxi­ mately 58 h. The bacteria change their metabolism in the famine phase and start using the PHA stored in the feast phase as carbon source for growth and maintenance. This shift is evidenced by the decrease in intracellular PHA over time during the famine period. Notably, a decrease in ammonium concentration is observed during both the feast and famine phases. Therefore, bacterial populations proficient in intracellular have enhanced growth and survival capabilities. In contrast, those with lower PHA storage capacity are competitively disadvantaged and are eliminated from the population after a sufficient number of F/F cycles. Table 1 provides a summary of key performance parameters observed across multiple F/F cycles after 1x, 2x and 3xHRTs. These data show that the initial microbiome evolved towards higher PHA storage capacity. The VSS was kept stable between 14 and 17 gDW/ L. The increase in intracellular PHA content is more pronounced after 2xHRTs. This experimental data were used to train the PINN as described in the next section.

## 3.2. PINN training on the historical data <a id="3-2-pinn-training-on-the-historical-data"></a>

The PINN model was trained using the historical data collected from the SBR system over a 93-day cultivation period, as described in the previous section. The data partition followed a time-based splitting strategy: the first 10 cycles were used for training (153 data points), the following 10 cycles were used for validation (113 data points) and the last 10 cycles were used for testing (61 data points). The hyper­ parameters that were investigated were the network size (number of hidden layers and number of nodes in hidden layers), ADAM hyper­ parameters (learning rate and number of epochs) and the relative weight of data and physics loss terms (hyperparameter λ ) ⊡ It was ensured in all tests performed that the number of data residuals plus the number of physics residuals is always larger than the number of PINN weights. The results are shown in Tables 2, 3 and 4 , indicating that all assessed pa­ rameters have a significant impact on the PINN training and validation performances. The PINN structure 25 × 25 was selected as best structure since it achieved the lowest validation data loss ( Q 2 = 0.95; Table 2 ). This structure also achieved the lowest training and testing data loss. The combination of a learning rate of 1.0 × 10 − 3 and 2000 epochs also yielded the lowest validation loss ( Table 3 ) and was selected in all subsequent studies. The hyperparameter, λ , plays a critical role in the PINN training ( Table 4 ). When λ = 0 the PINN training disregards the physical equations making it analogous to a conventional FFNN. This resulted in the lowest training data loss but yielded the second highest validation data loss. Conversely, setting λ = 1 causes the PINN to rely solely on an incomplete set of physical equations, disregarding data points entirely. This yielded the highest losses across training,
(7a)
(7b)
validation and testing. The best performance in both training and validation was achieved when λ = 0.5, where equal weight was given to
5


--- Page 6 ---


M. Catal ˜ ao et al. Journal of Process Control 156 (2025) 103594
Fig. 3. Dynamics of the Corroios Marshland microbiome in a sequencing batch reactor (SBR) operated with a hydraulic retention time (HRT) of 30 days. Con­ centration of volatile suspended solids (VSS, green) and intracellular polyhydroxyalkanoates content (PHA, red) over a 93-day period (3xHRT).
both the data and physics loss terms. It should be noted that the test data included very few data points thus the interpretation of the test Q 2
should be done with care. In summary, the optimal hyperparameter values were determined to be a network with two hidden layers with 25 nodes each, a learning rate of 1.0 × 10 − 3 , 2000 training epochs and a relative weight between data and physics loss of λ = 0.5. This optimal set of hyperparameters was applied to all subsequent studies.
Fig. 4 presents a comparison between experimental data and PINN predictions over time using the optimal set of hyperparameters and selected 25 × 25 PINN structure. These results show that the PINN effectively captured the dynamic behavior of acetate, ammonia, active biomass and intracellular PHA concentrations. Notably, the model shows strong performance in forecasting ammonia dynamics. Addi­ tionally, the PINN successfully predicted an increase in PHA storage capacity after day 30. Although the general dynamic patterns were accurately captured, a noticeable process – model mismatch is observed in several cycles, where predicted concentration values deviate signifi­ cantly from the measured data. This suggests that more data and higher quality data could improve the training results.
Artificial neural networks (ANNs) have been previously applied to model and optimize PHA production [44,45] . However, direct com­ parisons between physics-informed neural networks (PINNs) and ANNs in this context are lacking. Our results demonstrate that PINNs exhibit lower validation errors than standalone ANNs ( Table 3 ; λ = 0.5 vs. λ = 0, respectively). This observation is consistent with findings from other biological systems, where similar trends have been reported. Incorpo­ rating prior knowledge into the training of PINNs enhances their generalization ability and reduces dependence on large datasets compared to classical ANNs ( [46 – 49] ). The higher predictive accuracy may be a key advantage for the closed-loop performance of a MPC system [43] .
Hybrid models that integrate ANNs with mechanistic equations have also been reported in the literature for both pure cultures [50] and microbiomes [51] but the direct comparison with PINNs is lacking. Yang et al. [46] compared hybrid models with PINNs for a fed-batch CHO culture at pilot scale and concluded that the PINN exhibited superior predictive performance. In contrast, Jul-Rasmussen et al. [47] and Kumar Thirugnanasambandam [49] reported that hybrid semi­ parametric models outperformed PINNs in predictive accuracy. A direct comparison between PINNs and hybrid semiparametric models for PHA production remains to be established and should be addressed in future studies

## 3.3. Transfer learning <a id="3-3-transfer-learning"></a>

Given the relatively high prediction errors in some cycles of the historical data set, there is a significant risk of process-model mismatch during process control. To decrease the process-model mismatch a transfer learning scheme may be implemented, however, a key chal­ lenge is to timely update the model on the new domain without “ forgetting ” the historical domain.
We have firstly investigated how the PINN prediction error depends on the quantity of data. The PINN was initially trained using data of a single historical cycle, validated on the data of the following cycle and then on all other future cycles. As next step, the PINN was trained on 2 historical cycles and validated on the following and all future cycles. This procedure was repeated by increasing the number of historical cycles in the training data set. The training hyperparameters were the same as in the previous section. The results are given in Table 5 .
The results clearly show that the validation error decreases as more data is used for training. Conversely, the training error slightly increases as more data is used for training. In the first two iterations the validation error is 10-fold higher than the training error suggesting a significant overfitting of training data points. After 10 iterations (or 10 cycles used for training) the training and validation errors are close to each other denoting a well-balanced training. This suggests that data of 8 – 10 cycles should be included in the training data set in order to mitigate over­ fitting before the model could be used for process control.
In order to more effectively reduce the prediction error in the in- process cycle and ensure robust process control, a transfer learning scheme was implemented, utilizing both historical and in-process cycles data for training. There are different schemes of transfer learning pro­ posed in the literature [52] . In this study we apply a simple form of transductive parameter-transfer learning, where the source and target tasks are the same, but are applied in different domains. The different domains are assumed to share some PINN hyperparameters or prior distributions of such hyperparameters for the execution of the target task. The transfer learning scheme was implemented according to the following steps:
i) The PINN model trained and validated on the historical data set was directly transferred to the control experiment; ii) The data of a new in-process cycle (incremental cycle) combined with historical data was used to update the parameters of the PINN on the new domain. The learning algorithm was ADAM with stochastic regularization but with the probabilities of in-
6


--- Page 7 ---




| Table1   | ~ PHA in in Performance across the volumetric of the accumulation bioreactor the end of each . SBR HRT 30 parameters multiple (performed cycles including productivity days)   | PHA PHA ratio ratio bioreactor volumetric Accumulation bioreactor HRT TSS VSS Selection F/F C/N (g/L) (g/L) (mgPHA/gVSS) productivity (gPHA/(L⋅day))   | ± 1 12 ± 12 Initial microbiome 127 .90 .03 .6 0 .20 .5   | ± ± 12 1xHRT 93 .68 0 .05 13 .73 0 .00 0 .46 .5   | . . 089±0 077   | ± ± 1 12 .2 2xHRT 58 .18 0 .57 15 .25 0 .20 .5   | . . 5573 124   | ±580 ,   | ± 11 ± 3xHRT 52 .48 3 .17 .88 0 .62 0 .18 25   | . . 16877 184   | . ±381   |
|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|---------------------------------------------------|-----------------|--------------------------------------------------|----------------|----------|------------------------------------------------|-----------------|----------|




| 0-Network   | 1-R2       | 2-Q2         | 3-Q2      | 4-CPU     | 5-Numberof   |
|:------------|:-----------|:-------------|:----------|:----------|:-------------|
| size        | (training) | (validation) | (testing) | (seconds) | weights      |
| 10          | 090        | 083          | 094       | 560       | 148          |
|             | .          | .            | .         |           |              |
| 25          | 093        | 085          | 095       | 609       | 358          |
|             | .          | .            | .         |           |              |
| 50          | 093        | 089          | 095       | 611       | 708          |
|             | .          | .            | .         |           |              |
| 10×10       | 093        | 088          | 095       | 721       | 258          |
|             | .          | .            | .         |           |              |
| 25£25       | 098        | 095          | 098       | 615       | 618          |
|             | .          | .            | .         |           |              |
| 50×50       | 095        | 094          | 097       | 661       | 1218         |
|             | .          | .            | .         |           |              |
| 10x10x10    | 094        | 089          | 096       | 722       | 368          |
|             | .          | .            | .         |           |              |
| 25x25x25    | 094        | 092          | 096       | 815       | 1658         |
|             | .          | .            | .         |           |              |
| 50x50x50    | 093        | 091          | 096       | 744       | 5808         |
|             | .          | .            | .         |           |              |




| orresponded t ighlighted in Learning   | to the 21–3 bold. Epochs   | 30 cycles. The R2   | e selected hyper Q2   | rparameters p Q2   | performanc CPU   |
|:---------------------------------------|:---------------------------|:--------------------|:----------------------|:-------------------|:-----------------|
| Learning                               | Epochs                     | R2                  | Q2                    | Q2                 | CPU              |
| rate                                   |                            | (training)          | (validation)          | (testing)          | (seconds)        |
| 1 .0 × 10−2                            | 1000                       | 078                 | 076                   | 092                | 297              |
|                                        |                            | .                   | .                     | .                  |                  |
| 1 .0 × 10−2                            | 2000                       | 079                 | 078                   | 092                | 600              |
|                                        |                            | .                   | .                     | .                  |                  |
| 1 .0 × 10−2                            | 3000                       | 083                 | 081                   | 093                | 891              |
|                                        |                            | .                   | .                     | .                  |                  |
| 1 .0 × 10−3                            | 1000                       | 082                 | 080                   | 090                | 301              |
|                                        |                            | .                   | .                     | .                  |                  |
| 1 .0 £ 10¡3                            | 2000                       | 098                 | 095                   | 098                | 615              |
|                                        |                            | .                   | .                     | .                  |                  |
| 1 .0 × 10−3                            | 3000                       | 098                 | 095                   | 098                | 971              |
|                                        |                            | .                   | .                     | .                  |                  |
| 1 .0 × 10−4                            | 1000                       | 089                 | 087                   | 091                | 305              |
|                                        |                            | .                   | .                     | .                  |                  |
| 1 .0 × 10 −4                           | 2000                       | 089                 | 087                   | 091                | 614              |
|                                        |                            | .                   | .                     | .                  |                  |
| 1 .0 × 10−4                            | 3000                       | 089                 | 086                   | 091                | 912              |
|                                        |                            | .                   | .                     | .                  |                  |




| λvalue   | R2 (training)   | Q2 (validation)   | Q2 (testing)   |   CPU(seconds) |
|:---------|:----------------|:------------------|:---------------|---------------:|
| 000      | 099             | 082               | 097            |            631 |
| .        | .               | .                 | .              |                |
| 025      | 097             | 093               | 098            |            580 |
| .        | .               | .                 | .              |                |
| 050      | 098             | 095               | 098            |            615 |
| .        | .               | .                 | .              |                |
| 075      | 096             | 094               | 098            |            561 |
| .        | .               | .                 | .              |                |
| 100      | − 0 .54         | − 0 .58           | 020            |            612 |
| .        |                 |                   | .              |                |


M. Catal ˜ ao et al. Journal of Process Control 156 (2025) 103594
HRT TSS (g/L) VSS (g/L) F/F ratio C/N ratio PHA (mgPHA/gVSS) Selection bioreactor PHA volumetric productivity (gPHA/(L ⋅ day)) Accumulation bioreactor
Table 1 Performance parameters across multiple SBR cycles including the volumetric productivity of PHA in the accumulation bioreactor (performed in the end of each HRT ~ 30 days).
0.89 ± 0 0.77
55.73 ± 5,80 1.24
168.77 ± 3.81 1.84
Initial microbiome 127.90 ± 1.03 12.6 ± 0.20 12.5
1xHRT 93.68 ± 0.05 13.73 ± 0.00 0.46 12.5
2xHRT 58.18 ± 0.57 15.25 ± 1.2 0.20 12.5
3xHRT 52.48 ± 3.17 11.88 ± 0.62 0.18 25
Table 2 Results for various network sizes. Number of epochs was set to 2000, learning rate was set to 1.0 × 10 − 3 and λ was set to 0.5. The number of collocation points was 2000. Training data corresponded to the first 10 cycles. Validation data corresponded to the 11 – 20 cycles. Testing data corresponded to the 21 – 30 cy­ cles. The selected PINN model performance is highlighted in bold.
CPU (seconds)
Network size
R 2
Q 2
Q 2
(training)
(validation)
(testing)
10 0.90 0.83 0.94 560 148 25 0.93 0.85 0.95 609 358 50 0.93 0.89 0.95 611 708 10 × 10 0.93 0.88 0.95 721 258 25 £ 25 0.98 0.95 0.98 615 618 50 × 50 0.95 0.94 0.97 661 1218 10x10x10 0.94 0.89 0.96 722 368 25x25x25 0.94 0.92 0.96 815 1658 50x50x50 0.93 0.91 0.96 744 5808
Table 3 Results for various training parameters (learning rate and epochs). Network size was set to 25 × 25 and λ was set to 0.5. Training data corresponded to the 10 first cycles. Validation data corresponded to the 11 – 20 cycles. Testing data corresponded to the 21 – 30 cycles. The selected hyperparameters performance is highlighted in bold.
Learning rate
Epochs R 2
Q 2
Q 2
(training)
(validation)
(testing)
1.0 × 10 − 2 1000 0.78 0.76 0.92 297 1.0 × 10 − 2 2000 0.79 0.78 0.92 600 1.0 × 10 − 2 3000 0.83 0.81 0.93 891 1.0 × 10 − 3 1000 0.82 0.80 0.90 301 1.0 £ 10 ¡ 3 2000 0.98 0.95 0.98 615 1.0 × 10 − 3 3000 0.98 0.95 0.98 971 1.0 × 10 − 4 1000 0.89 0.87 0.91 305 1.0 × 10 − 4 2000 0.89 0.87 0.91 614 1.0 × 10 − 4 3000 0.89 0.86 0.91 912
Table 4 Results for various experimental/physics loss weighting factors ( λ value). Network size was set to 25 × 25, learning rate was set to 1.0 × 10 − 3 and number of epochs was set to 2000. The selected hyperparameters performance is high­ lighted in bold.
λ value R 2 (training) Q 2 (validation) Q 2 (testing) CPU (seconds)
0.00 0.99 0.82 0.97 631 0.25 0.97 0.93 0.98 580 0.50 0.98 0.95 0.98 615 0.75 0.96 0.94 0.98 561 1.00 − 0.54 − 0.58 0.20 612
process and historical data points set to 0.75 and 0.25 respec­ tively ( Table 6 ). This gives more importance to the in-process data points than historical data points. All other hyper­ parameters were the same as for historical training; iii) Four different metrics were evaluated, R 2 of the historical cycles (training), R 2 of the in-process cycle (training), Q 2 of future cycles (validation) and CPU for training. iv) Steps ii) to iv) were repeated for additional incremental cycles.
This approach was initially evaluated starting with the PINN trained and validated on the historical data set (results of the previous section). Cycles 21 – 25 were set as incremental in-process cycles. The overall re­ sults are shown in Table 6 for different probabilities of historical and in- process datapoints. In all cases, it is possible to observe a slight improvement in the predictive capabilities of the PINN as it receives more data from the incremental in-process cycles. The in-process pre­ diction error progressively decreases and approaches that of historical cycles. The prediction error of future cycles also improves progressively.
7
Number of weights
CPU (seconds)


--- Page 8 ---


M. Catal ˜ ao et al. Journal of Process Control 156 (2025) 103594

![[Bio-Process_img_5fdf4b97ca.jpeg]]

Fig. 4. Training and validation results for the selected 25 × 25 PINN structure with optimal hyperparameters (learning rate = 1.0 × 10 ⁻ ³, 2000 epochs, and λ = 0.5). Circles represent training data, while crosses represent validation data. The solid line indicates parity, and the dashed lines denote a 10 % error interval. The obtained R² values for Acetate, Ammonia, Biomass, and fPHA are 0.98, 0.99, 0.92, and 0.23, respectively. The corresponding Q² values are 0.96, 0.97, 0.86, and 0.53.
8


--- Page 9 ---




| Training   | Training loss   | Following cycle   | Future cycles   | CPU time   |
|:-----------|:----------------|:------------------|:----------------|:-----------|
| Training   | Trainingloss    | Followingcycle    | Futurecycles    | CPUtime    |
| cycles     | (R2)            | loss(Q2)          | loss(Q2)        | (seconds)  |
| 1          | 099             | 018               | 016             | 565        |
|            | .               | .                 | .               |            |
| 1–2        | 099             | 015               | − 0 .12         | 602        |
|            | .               | .                 |                 |            |
| 1–3        | 099             | 042               | 054             | 599        |
| 1–4        | .               | .                 | .               | 608        |
| 1–5        | 099             | 082               | 078             | 622        |
|            | .               | .                 | .               |            |
|            | 099             | 090               | 086             |            |
|            | .               | .                 | .               |            |
| 1–6        | 098             | 095               | 090             | 615        |
|            | .               | .                 | .               |            |
| 1–7        | 098             | 096               | 092             | 691        |
|            | .               | .                 | .               |            |
| 1–8        | 098             | 093               | 089             | 633        |
|            | .               | .                 | .               |            |
| 1–9        | 099             | 097               | 096             | 651        |
| 1–10       | .               | .                 | .               | 615        |
|            | 098             | 097               | 095             |            |
|            | .               | .                 | .               |            |




| Case         | Metrics         | Predict   | tion cycles   | Col4   | Col5   | Col6   |
|:-------------|:----------------|:----------|:--------------|:-------|:-------|:-------|
| Case         | Metrics         | Predic    | tioncycles    |        |        |        |
|              |                 | 21        | 21–22         | 21–23  | 21–24  | 21–25  |
| Case1:       | Historicaldata  | 096       | 097           | 097    | 097    | 098    |
| phist= 0 .25 | loss(R2)        | .         | .             | .      | .      | .      |
| pInP= 0 .75  | In-process data | 091       | 092           | 094    | 095    | 096    |
|              | loss(R2)        | .         | .             | .      | .      | .      |
|              | Futurecycles    | 080       | 081           | 085    | 089    | 090    |
|              |                 | .         | .             | .      | .      | .      |
|              | loss(Q2)        |           |               |        |        |        |
|              | CPUtime         | 627       | 631           | 614    | 677    | 613    |
| Case2:       | (seconds)       | 098       | 098           | 099    | 098    | 099    |
| phist = 0 .5 | Historicaldata  | .         | .             | .      | .      | .      |
| pInP = 0 .5  | loss(R2)        | 085       | 085           | 086    | 089    | 088    |
|              | In-process data | .         | .             | .      | .      | .      |
|              | loss(R2)        |           |               |        |        |        |
|              | Futurecycles    | 079       | 080           | 082    | 086    | 084    |
|              |                 | .         | .             | .      | .      | .      |
|              | loss(Q2)        |           |               |        |        |        |
| Case3:       | CPUtime         | 651       | 605           | 671    | 644    | 683    |
| phist= 0 .75 | (seconds)       | 099       | 099           | 099    | 099    | 099    |
|              | Historicaldata  | .         | .             | .      | .      | .      |
|              | loss(R2)        |           |               |        |        |        |
| pInP= 0 .25  | In-process data | 084       | 076           | 079    | 082    | 081    |
|              |                 | .         | .             | .      | .      | .      |
|              | loss(R2)        |           |               |        |        |        |
|              | Futurecycles    | 080       | 079           | 077    | 081    | 079    |
|              | loss(Q2)        | .         | .             | .      | .      | .      |
|              | CPUtime         | 604       | 623           | 655    | 653    | 642    |
| Case4:       | (seconds)       | 098       | 099           | 099    | 099    | 098    |
|              | Historicaldata  | .         | .             | .      | .      | .      |
| Full         | loss(R2)        | 064       | 071           | 066    | 073    | 079    |
| retraining   | In-process data | .         | .             | .      | .      | .      |
|              | loss(R2)        |           |               |        |        |        |
|              | Futurecycles    | 072       | 076           | 071    | 074    | 079    |
|              | loss(Q2)        | .         | .             | .      | .      | .      |
|              | CPUtime         | 681       | 714           | 692    | 677    | 701    |
|              | (seconds)       |           |               |        |        |        |


M. Catal ˜ ao et al. Journal of Process Control 156 (2025) 103594
Table 5 Evolution of the PINN predictive power as the number of training cycles in­ creases. Previously determined optimal hyperparameters were used (Network size of 25 × 25, learning rate of 1.0 × 10 − 3 , 2000 epochs and λ = 0.5).
Training cycles
Training loss ( R 2 )
Following cycle loss ( Q 2 )
Future cycles loss ( Q 2 )
CPU time (seconds)
1 0.99 0.18 0.16 565 1 – 2 0.99 0.15 − 0.12 602 1 – 3 0.99 0.42 0.54 599 1 – 4 0.99 0.82 0.78 608 1 – 5 0.99 0.90 0.86 622 1 – 6 0.98 0.95 0.90 615 1 – 7 0.98 0.96 0.92 691 1 – 8 0.98 0.93 0.89 633 1 – 9 0.99 0.97 0.96 651 1 – 10 0.98 0.97 0.95 615
Table 6 Effect of transfer learning in the PINN predictive power. Historical data points and in-process data points were randomly selected with p hist and p InP probabilities, respectively (Case 1 – 3). Case 4 represents a baseline sce­ nario where full retraining is performed with all historical and all in process data points together. Previously determined optimal hyperparameters were used (Network size of 25 × 25, learning rate of 1.0 × 10 − 3 , 2000 epochs and λ = 0.5).
Case Metrics Prediction cycles
21 21 – 22 21 – 23 21 – 24 21 – 25
Case 1: p hist = 0.25 p InP = 0.75
Historical data loss ( R 2 )
0.96 0.97 0.97 0.97 0.98
In-process data loss ( R 2 )
0.91 0.92 0.94 0.95 0.96
0.80 0.81 0.85 0.89 0.90
Future cycles loss ( Q 2 )
CPU time (seconds)
627 631 614 677 613
Case 2: p hist = 0.5 p InP = 0.5
Historical data loss ( R 2 )
0.98 0.98 0.99 0.98 0.99
0.85 0.85 0.86 0.89 0.88
In-process data loss ( R 2 )
Future cycles loss ( Q 2 )
0.79 0.80 0.82 0.86 0.84
CPU time (seconds)
651 605 671 644 683
Case 3: p hist = 0.75 p InP = 0.25
Historical data loss ( R 2 )
0.99 0.99 0.99 0.99 0.99
In-process data loss ( R 2 )
0.84 0.76 0.79 0.82 0.81
Future cycles loss ( Q 2 )
0.80 0.79 0.77 0.81 0.79
CPU time (seconds)
604 623 655 653 642
Case 4: Full retraining
Historical data loss ( R 2 )
0.98 0.99 0.99 0.99 0.98
In-process data loss ( R 2 )
0.64 0.71 0.66 0.73 0.79
Future cycles loss ( Q 2 )
0.72 0.76 0.71 0.74 0.79
CPU time (seconds)
681 714 692 677 701
The highest predictive power was achieved with a selection probability of historical and in-process data points of 0.25 and 0.75 respectively. This result was further compared with a baseline scenario where the PINN is retrained with all historical and in-process data points together. In this case, it is possible to observe that lower training errors were obtained when compared to the incrementally trained PINN. On the other hand, the prediction error for future cycles, while showing small improvements, is higher than the incrementally trained model. In conclusion, with the probabilities of historical data points and in-process data points set to 0.25 and 0.75 respectively, the prediction of in-process and future cycles is improved while the historical data is not forgotten as
the R 2 slightly increases. Furthermore, the required CPU is approxi­ mately 10 mins, which is perfectly acceptable for the control problem at hand.

## 3.4. Process control experiment <a id="3-4-process-control-experiment"></a>

A new SBR selection experiment was initiated with an unevolved microbiome collected from the same site of the historical data set experiment. The new SBR experiment was conducted under automatic control of the PINN-MPC with transfer learning according to the following steps:
i) The PINN trained and validated on the historical data set (results of Section 3.2 ) was directly transferred for the process control experiment; ii) Transfer learning was implemented as described in the previous section ( Table 6 ). As process data is collected off-line, new data availability was irregular, namely at cycles 2, 5 and 10; iii) 3-factors CCD optimization heuristic based on the PINN forecast of 20 cycles in the future in order to optimize the control inputs ( HRT , OLR , NLR ) to be applied in the following cycle; iv) Control action of the peristaltic pumps to enforce the optimal control parameters identified at step iii) into the real process; v) Repeat steps ii)-iv) for every new cycle. Step ii) was only con­
ducted when new off-line data was available from the lab;
The first 2 cycles were manually operated whereas the following cycles were operated under automatic control. The optimization of cycle k = 4 is illustrated in Fig. 5 . A CCD with 3 factors ( OLR , NLR , HRT ) and 5 levels (-1.6818, − 1, 0, 1, 1.6818) was applied over the control design space. The PINN was simulated for each CCD experiment 20 cycles in the future ( Fig. 5 B). Response surface analysis identified the optimal oper­ ating point that maximizes PHA volumetric concentration 20 cycles in the future (response variable) ( Fig. 5 A). Fig. 5 A shows the dependency of the response variable over specific OLR and NRL. It should be noted that the upper boundary of volume of purge (400 mL corresponding to HRT = 15 days) was consistently chosen by the PINN as the optimal value. For this reason, HRT was excluded from the response surface analysis. Fig. 5 A shows two different regions that maximize volumetric PHA concentration, either aligned along the maximum specific OLR or aligned along the maximum specific NLR . The optimal control decision was HRT = 15 days, OLR = 0.208 g/gVSS × d, NLR = 0.010 g/gVSS × d (C/N = 20.8 g/g). The PINN simulation at the optimal control point is shown in Fig. 5 B. The PINN forecasted a progressive increase in the intracellular PHA concentration, stabilizing between 200 and 250 mg/ gVSS in the last 4 cycles. Contrary to this, the VSS is forecasted to decrease over time and stabilizes close to 6 gVSS/L. This reflects the trade-off between promoting biomass growth or intracellular PHA storage. The PINN decision sacrificed growth in relation to intracellular PHA storage.
Cycle-to-cycle PINN-MPC was repeated for every new cycle up to k = 12 cycles corresponding to 30 days and 2xHRT. At the end of cycle 12 the experiment was stopped due to operational limitations in the lab. The PINN was trained by transfer learning whenever new off-line data was available from the lab, namely at the end of cycles 2, 5 and 10. The effect of transfer learning in the prediction accuracy of state variables is summarized in Table 7 . The prediction accuracy at cycle 2 was not satisfactory except for the case of acetate. However, the 3 transfer learning events substantially improved the PINN yielding much lower MSE and progressively higher Q 2 for the 4 state variables.
The overall control results for the remaining cycles are shown in Fig. 6 A-D. Fig. 6 A shows the cycle-to-cycle evolution of control vari­ ables. There is a clear tendency to increase the specific OLR and NRT over cycle. As previously mentioned, the HRT was consistently opti­ mized at the minimum value allowed of 15 days. This suggests that as the evolution progresses towards more efficient microbiomes, the
9


--- Page 10 ---




| In-process   | Biomass   | Ammonium   | Acetate   | PHA   | Relative   |
|:-------------|:----------|:-----------|:----------|:------|:-----------|
| In-process   | Biomass   | Ammonium   | Acetate   | PHA   | Relative   |
| cycle        | (Q2)      | (Q2)       | (Q2)      | (Q2)  | MSE(%)     |
| 1            | -         | -          | -         | -     | 32         |
| 2(*)         | 051       | 057        | 098       | 036   | 35         |
| 3            | .         | .          | .         | .     | 27         |
| 4            | -         | -          | 087       | -     | 5          |
|              | -         | -          | .         | 099   |            |
|              |           |            | -         | .     |            |
| 5(*)         | -         | 098        | 094       | 085   | 24         |
|              |           | .          | .         | .     |            |
| 6            | -         | -          | -         | -     | 6          |
| 7            | 072       | -          | 097       | 091   | 14         |
| 8            | .         | -          | .         | .     | 6          |
| 9            | 092       | -          | 081       | 099   | 10         |
|              | .         |            | .         | .     |            |
|              | -         |            | -         | -     |            |
| 10(*)        | 065       | -          | 098       | 097   | 15         |
|              | .         |            | .         | .     |            |
| 11           | -         | -          | -         | -     | 6          |
| 12           | -         | -          | -         | -     | 7          |


M. Catal ˜ ao et al. Journal of Process Control 156 (2025) 103594

![[Bio-Process_img_8bfec93870.jpeg]]

Fig. 5. PINN prediction and CCD optimization of cycle k = 4. A - response surface, where the X corresponds to the optimal conditions; B - PINN forecast 20 cycles in the future at the optimal operating point ( HRT = 15 days, OLR = 0.208 g/gVSS × d, NLR = 0.010 g/gVSS × d (C/N = 20.8 g/g)). These conditions are suggested to increase the intracellular PHA and total PHA despite reducing the amount of VSS.
Table 7 Evolution of the prediction error during the process control experiment. Error metrics refer to the in-process cycle under control. The index (*) marks transfer learning steps using data of all previous in-process cycles. The probabilities of in- process and historical data points were set to 0.75 and 0.25 respectively. Pre­ viously determined optimal hyperparameters were used (Network size of 25 × 25, learning rate of 1.0 × 10 − 3 , 2000 epochs and λ = 0.5). Missing values are due to less than 3 data points available to calculate Q 2 .
In-process cycle
Biomass ( Q 2 )
Ammonium ( Q 2 )
Acetate ( Q 2 )
PHA ( Q 2 )
Relative MSE (%)
1 - - - - 32 2(*) 0.51 0.57 0.98 0.36 35 3 - - 0.87 - 27 4 - - - 0.99 5 5(*) - 0.98 0.94 0.85 24 6 - - - - 6 7 0.72 - 0.97 0.91 14 8 0.92 - 0.81 0.99 6 9 - - - - 10 10(*) 0.65 - 0.98 0.97 15 11 - - - - 6 12 - - - - 7
amount of carbon and nitrogen should be progressively increased on a per cell basis. In general, the PINN predictions of in-process VSS, intracellular PHA and volumetric PHA concentrations at the end of the feast phase follow closely the measured data. As a consequence of the
control decisions, the VSS concentration decreased from 13.35 gVSS/L at cycle k = 0 – 6.74 gVSS/L at cycle 12 ( Fig. 6 B). The PINN predicted a smooth transition between cycles 4 and 7 whereas the real process transition was sharper at cycle 5. Opposed to VSS, a systematic increase of both the intracellular PHA concentration ( Fig. 6 C) and volumetric PHA concentration ( Fig. 6 D) were observed. The intracellular PHA concentration increased from 7 to 165 mg/gVSS at cycle 12 (23-fold increase). The volumetric PHA concentration increased from 65 to 1112 mg/L (17-fold increase). This shows that the intracellular increase in PHA concentration counteracted the VSS increase resulting in a 17- fold increase of overall PHA production. This may suggest that there is a trade-off between growth metabolism and PHA storage metabolism that was however faithfully captured by the PINN. The PINN controlled experiment may be compared to the historical data SBR experiment in the first 2xHRT. The historical data SBR was operated under constant HRT = 30 days, OLR = 1.67 gCOD/Ld and C/N = 22.73 gCOD/gN. The VSS and PHA concentrations in the SBR reached 16.43 gVSS/L and 915 mg/L respectively after 2xHRT (60 days of operation). Thus the PINN control experiment achieved a 21.5 % higher PHA concentration in half of the time compared to the historical experiment.

## 3.5. PHA production experiment <a id="3-5-pha-production-experiment"></a>

The final evolved microbiome, collect at the end of the famine phase of cycle 12 (36 days) of the PINN controlled experiment, was inoculated in the production bioreactor to assess the maximum PHA accumulation capacity. This reactor was operated in fed-batch mode under the same operational conditions as the selection SBR, except for the acetate and ammonia feeding strategy. Four pulses were administered at times 0 h, 11h30, 17 h and 42 h under automatic on-line control based on the dissolved oxygen sensor. Ammonium chloride (0.21 g N/L) was co-fed only in the first pulse. Fig. 7 shows the obtained time profiles. VSS increased from 6.57 ± 0.56 – 15.67 ± 0.36 g/L. The PHA content increased from ~0 – 52.86 ± 3.2 wt%, corresponding to 8.28 gPHA/L. Over the 42 h of cultivation, the culture consumed 19.40 g/L acetate and produced 8.93 g PHA/L, yielding a maximum volumetric produc­ tivity of 5.10 gPHA/Ld and a yield of 0.46 gPHA/g acetate.

## 4. Conclusions <a id="4-conclusions"></a>

PINNs are a recent machine learning framework that learns simul­ taneously from experimental data and mathematical equations. They have lower dependency on the amount of data and have higher pre­ dictive power comparatively to conventional neural networks. Furthermore, PINN-based dynamic simulation is generally fast compared to systems of differential equations making them well-suited for MPC applications. In this study, a PINN framework was applied for the first time for dynamic modelling and MPC of microbiome dynamics in a SBR process. The PINN dynamic model was trained on historical data of a SBR experiment and then directly transferred to a different SBR experiment. The PINN-MPC was tasked to adjust the HRT, OLR and NLR cycle-to-cycle such as to maximize PHA volumetric concentration 20 cycles in the future This approach can generate a time-varying profile for the control degrees of freedom to achieve optimal performance, which may offer an advantage over the constant control strategies commonly reported in the literature. To minimize model-process mismatch, a transductive parameter-transfer learning scheme was implemented. Overall, the natural microbiome has evolved over time showing a suc­ cessful PHA volumetric concentration increase from 65 to 1112 mg/L (17-fold increase) over a time frame of 60 days (2xHRT). This goal was attained through two counteracting factors. The biomass concentration decreased from 13.35 gVSS/L to 6.74 gVSS (49.5 % decrease). This was compensated by a much larger increase in intracellular PHA concen­ tration from 7 to 165 mg/gVSS at (23-fold increase). Moreover, the PINN predictions closely aligned with the in-process experimental data. The developed PINN system bears the capacity to learn in autonomy
10


--- Page 11 ---


M. Catal ˜ ao et al. Journal of Process Control 156 (2025) 103594

![[Bio-Process_img_c5c465d566.jpeg]]

Fig. 6. (A) Chosen Specific Organic Loading Rate (OLR) (blue) and Specific Nitrogen Loading Rate (NLR) (black) over cycle. (B-D) Comparison between experi­ mental and predicted concentration by the PINN-MPC controller. Full bars are experimental value. Filled bars are measured values and open bars are PINN predicted values for ( B ) VSS concentration (g/L) (green). ( C ) PHA intracellular concentration (mg/g) (red). ( D ) PHA volumetric concentration (g/L) (orange).

![[Bio-Process_img_7e37f3591d.jpeg]]

Fig. 7. Accumulation assay in the production reactor inoculated with the purge of the PINN controlled SBR at cycle 12 (~ 2xHRT). Time profiles of PHA (%) ( ), VSS (g/L) (orange columns), acetate (g/L) ( ● ) and ammonium (g/L) ( ). Results shown both an overall increase in VSS and intracellular PHA as the accumula­ tion proceeds.
11


--- Page 12 ---


M. Catal ˜ ao et al. Journal of Process Control 156 (2025) 103594
from historical and in-process data. With each additional cycle, the system can progressively reduce the discrepancy between the process and the model, thereby improving process control robustness.

## CRediT authorship contribution statement <a id="credit-authorship-contribution-statement"></a>

Jos ´ e Pinto: Writing – review & editing, Writing – original draft, Visualization, Validation, Software, Methodology, Formal analysis. Marta Catal ˜ ao: Writing – review & editing, Writing – original draft, Visualization, Validation, Methodology, Investigation, Formal analysis, Data curation. Rui Oliveira: Writing – review & editing, Writing – original draft, Supervision, Project administration, Funding acquisition, Conceptualization. Rafael S. Costa: Writing – review & editing, Meth­ odology, Conceptualization. Maria A.M. Reis: Supervision, Project administration, Funding acquisition, Conceptualization. Filomena Freitas: Writing – review & editing, Supervision, Project administration, Funding acquisition, Conceptualization. Cristiana A.V. Torres: Writing – review & editing, Supervision, Methodology, Conceptualization.

## Declaration of Competing Interest <a id="declaration-of-competing-interest"></a>

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgements <a id="acknowledgements"></a>

This work is financed by national funds from FCT - Fundaç ˜ ao para a Ci ˆ encia e a Tecnologia, I.P., in the scope of the project UIDP/04378/ 2020 (DOI: 10.54499/UIDP/04378/2020) and UIDB/04378/2020 (DOI: 10.54499/UIDB/04378/2020) of the Research Unit on Applied Molecular Biosciences - UCIBIO and the project LA/P/0140/2020 (DOI: 10.54499/LA/P/0140/2020) of the Associate Laboratory Institute for Health and Bioeconomy - i4HB. MC acknowledges the PhD grants 2023.02867.BD. JP acknowledges the post doctoral research grant with reference code H2020-FNR-12 – 2020 – Harnessing the power of Nature through productive microbial consortia in biotechnology - measure, model, master (PROMICON)" #NOVAID-B178.

## Data availability <a id="data-availability"></a>


## Data will be made available on request. <a id="data-will-be-made-available-on-request"></a>


## References <a id="references"></a>

[1] M. Raissi, P. Perdikaris, G.E. Karniadakis, Physics-informed neural networks: a deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations, J. Comput. Phys. 378 (2019) 686 – 707, https://doi.org/10.1016/j.jcp.2018.10.045 . [2] D.C. Psichogios, L.H. Ungar, A hybrid neural network-first principles approach to process modeling, AIChE J. 38 (10) (1992) 1499 – 1511, https://doi.org/10.1002/ aic.690381003 . [3] M.L. Thompson, M.A. Kramer, Modeling chemical processes using prior knowledge and neural networks, AIChE J. 40 (1994), https://doi.org/10.1002/ aic.690400806 . [4] R. Oliveira, Combining first principles modelling and artificial neural networks: a general framework, Comput. Chem. Eng. 28 (5) (2004) 755 – 766, https://doi.org/ 10.1016/j.compchemeng.2004.02.014 . [5] X. Jin, S. Cai, H. Li, G.E. Karniadakis, NSFnets (Navier-Stokes flow nets): physics- informed neural networks for the incompressible Navier-Stokes equations, J. Comput. Phys. 426 (2021) 109951, https://doi.org/10.1016/j.jcp.2020.109951 . [6] Z. Mao, A.D. Jagtap, G.E. Karniadakis, Physics-informed neural networks for high- speed flows, Comput. Methods Appl. Mech. Eng. 360 (2020) 112789, https://doi. org/10.1016/j.cma.2019.112789 . [7] B. Mahanty, Hybrid modeling in bioprocess dynamics: structural variabilities, implementation strategies, and practical challenges, Biotechnol. Bioeng. 120 (8) (2023) 2072 – 2091, https://doi.org/10.1002/bit.28503 . [8] J. Xie, H. Li, S. Su, J. Cheng, Q. Cai, H. Tan, L. Zu, X. Qu, H. Han, Quantitative analysis of molecular transport in the extracellular space using physics-informed neural network, Comput. Biol. Med. 171 (2024) 108133, https://doi.org/10.1016/ j.compbiomed.2024.108133 .
[9] Z. Hao, S. Liu, Y. Zhang, C. Ying, Y. Feng, H. Su, J. Zhu, Physics-informed machine learning: a survey on problems, Methods Appl. (2022) 1 – 45. 〈 http://arxiv. org/abs/2211.08064 〉 . [10] G.E. Karniadakis, I.G. Kevrekidis, L. Lu, P. Perdikaris, S. Wang, L. Yang, Physics- informed machine learning, Nat. Rev. Phys. 3 (6) (2021) 422 – 440, https://doi.org/ 10.1038/s42254-021-00314-5 . [11] J. Pateras, P. Rana, P. Ghosh, A taxonomic survey of physics-informed machine learning, Appl. Sci. 13 (12) (2023) 6892, https://doi.org/10.3390/app13126892 . [12] H. Zhao, O.J. Hao, T.J. McAvoy, C.-H. Chang, Modeling nutrient dynamics in sequencing batch reactor, J. Environ. Eng. 123 (4) (1997) 311 – 319, https://doi. org/10.1061/(ASCE)0733-9372(1997)123:4(311) . [13] T. Cui, T. Bertalan, N. Ndahiro, P. Khare, M. Betenbaugh, C. Maranas, I. G. Kevrekidis, Data-driven and physics informed modeling of Chinese Hamster Ovary cell bioreactors, Comput. Chem. Eng. 183 (2024) 108594, https://doi.org/ 10.1016/j.compchemeng.2024.108594 . [14] M. Mowbray, T. Savage, C. Wu, Z. Song, B.A. Cho, E.A. Del Rio-Chanona, D. Zhang, Machine learning for biochemical engineering: a review, Biochem. Eng. J. 172 (April) (2021) 108054, https://doi.org/10.1016/j.bej.2021.108054 . [15] A.W. Rogers, I.O.S. Cardenas, E.A. Del Rio-Chanona, D. Zhang, Investigating physics-informed neural networks for bioprocess hybrid model construction, in: Computer Aided Chemical Engineering, 52, Elsevier, 2023, pp. 83 – 88, https://doi. org/10.1016/B978-0-443-15274-0.50014-7 . [16] J.H. Lagergren, J.T. Nardini, R.E. Baker, M.J. Simpson, K.B. Flores, Biologically- informed neural networks guide mechanistic modeling from sparse experimental data, PLOS Comput. Biol. 16 (12) (2020) e1008462, https://doi.org/10.1371/ journal.pcbi.1008462 . [17] A. Yazdani, L. Lu, M. Raissi, G.E. Karniadakis, Systems biology informed deep learning for inferring parameters and hidden dynamics, PLOS Comput. Biol. 16 (11) (2020) e1007575, https://doi.org/10.1371/journal.pcbi.1007575 . [18] N.A. Daryakenari, M. De Florio, S. Khemraj, G.E. Karniadakis, AI-Aristotle: a physics-informed framework for systems biology gray-box identification, PLOS Comput. Biol. 20 (3) (2024) e1011916, https://doi.org/10.1371/journal. pcbi.1011916 . [20] T. Asrav, E. Aydin, Physics-informed recurrent neural networks and hyper- parameter optimization for dynamic process systems, Comput. Chem. Eng. 173 (January) (2023) 108195, https://doi.org/10.1016/j.compchemeng.2023.108195 . [21] Jianmu Su, et al., "Soil conditions and the plant microbiome boost the accumulation of monoterpenes in the fruit of Citrus reticulata ‘Chachi, Microbiome 11 (1) (2023) 61, https://doi.org/10.1186/s40168-023-01504-2 . [22] Pardeep Singh, et al., "Bioremediation: a sustainable approach for management of environmental contaminants. Abatement of environmental pollutants, Elsevier, 2020, pp. 1 – 23, https://doi.org/10.1016/B978-0-12-818095-2.00001-1 . [23] Sonu Sharma, et al., "Recent advances and mechanisms of microbial bioremediation of nickel from wastewater, Environ. Sci. Pollut. Res. 31 (28) (2024) 40224 – 40244, https://doi.org/10.1007/s11356-023-30556-y . [24] Shreya Sharma, Shilpa Sharma, "Microbial biotechnology for circular economy in wastewater treatment: potentials, technologies, and challenges. Advanced and Innovative Approaches of Environmental Biotechnology in Industrial Wastewater Treatment, Springer Nature Singapore, Singapore, 2023, pp. 1 – 21, https://doi.org/ 10.1007/978-981-99-2598-8_1 . [25] Ming Zhou, "Recent progress on the development of biofuel cells for self-powered electrochemical biosensing and logic biosensing: a review, Electroanalysis 27 (8) (2015) 1786 – 1810, https://doi.org/10.1002/elan.201500173 . [26] Etienne Paul, et al., "Biopolymers production from wastes and wastewaters by mixed microbial cultures: strategies for microbial selection, Waste Biomass.. Valoriz. 12 (8) (2021) 4213 – 4237, https://doi.org/10.1007/s12649-020-01252-6 . [27] Karolin Dietrich, et al., "Producing PHAs in the bioeconomy — Towards a sustainable bioplastic, Sustain. Prod. Consum. 9 (2017) 58 – 70, https://doi.org/ 10.1016/j.spc.2016.09.001 . [28] G. Novelli, P. Castellani, V. Conca, M. Majone, F. Valentino, Polyhydroxyalkanoate (PHA) production via resource recovery from industrial waste streams: a review of techniques and perspectives, Bioresour. Technol. 331 (2021) 124985, https://doi. org/10.1016/j.biortech.2021.124985 . [29] M. Matos, R.A.P. Cruz, P. Cardoso, F. Silva, E.B. Freitas, G. Carvalho, M.A.M. Reis, Combined strategies to boost poly-hydroxyalkanoate production from fruit waste in a three-stage pilot plant, ACS Sustain. Chem. Eng. 9 (2021) 8270 – 8279, https:// doi.org/10.1021/acssuschemeng.1c02432 . [30] G. Salvatori, A. Marchetti, A.M. Russo, J. Rodriguez, V. Scerbacov, F. Fianelli, S. Alfano, S. Crognale, A. Massimi, S. Rossetti, G. Canali, T. De Micheli, D. Bolzonella, M. Villano, Pilot-scale acidogenic fermentation of reground pasta byproduct for polyhydroxyalkanoate production with mixed microbial cultures, ACS Sustain. Chem. Eng. 13 (8) (2025) 3024 – 3035, https://doi.org/10.1021/ acssuschemeng.4c03754 . [31] A. Giovanella, M. Carvalheira, M. Grana, M.A.M. Reis, B.C. Marreiros, Impacto f saline osmotic stress on halotolerant polyhydroxyalkanoate (PHA)-accumulating mixed microbial cultures: boosting PHA production by osmotic downshock, J. Environ. Chem. Eng. 13 (3) (2025) 116521, https://doi.org/10.1016/j. jece.2025.116521 . [32] C. Magonara, E. Montagnese, D. Bertasini, C. Vona, G. Salvatori, L.N. Tayou, M. Villano, F. Battista, N. Frison, D. Bolzonella, G. Pesante, Mixed-culture polyhydroxyalkanoate production with variable hydroxyvalerate content from agri-food residues, Environ. Sci. Pollut. Res. (2024), https://doi.org/10.1007/ s11356-025-36316-4 . [33] G. Mannina, D. Presti, G. Montiel-Jarillo, J. Carrera, M.E. Su ´ arez-Ojeda, Recovery of polyhydroxyalkanoates (PHAs) from wastewater: a review, Bioresour. Technol. 297 (2019) 122478, https://doi.org/10.1016/j.biortech.2019.122478 .
12


--- Page 13 ---


M. Catal ˜ ao et al. Journal of Process Control 156 (2025) 103594
[34] L. Lorini, M. Majone, A. Sapienza, "High rate selection of PHA accumulating mixed cultures in sequencing batch reactors with uncoupled carbon and nitrogen feeding, N. Biotechnol. 56 (2020) 140 – 148, https://doi.org/10.1016/j.nbt.2019.11.003 . [35] R. Morya, F.H. Andrianantenaina, A.K. Pandey, Y.H. Yoon, S. Kim, Polyhydroxyalkanoate production from rice straw hydrolysate: insights into feast- famine dynamics and microbial community shifts, Chemosphere 341 (2023) 139967, https://doi.org/10.1016/j.chemosphere.2023.139967 . [36] S.T. Nguyen-Huynh, A.S.M. Chua, Y.H. Chow, W.Y. Wong, L.W. Yoon, Enrichment strategies for mixed cultures in valorisation of crude glycerol into polyhydroxyalkanoate bioplastics, Biochem. Eng. J. 200 (2023) 109086, https:// doi.org/10.1016/j.bej.2023.109086 . [37] 〈 https://cmbio.io/ 〉 . [38] D. McDonald, Y. Jiang, M. Balaban, et al., Greengenes2 unifies microbial data in a single reference tree, Nat. Biotechnol. 42 (2024) 715 – 718, https://doi.org/ 10.1038/s41587-023-01845-1 . [39] M. Diao, S. Dyksma, E. Koeksoy, D.K. Ngugi, K. Anantharaman, A. Loy, M. Pester, Global diversity and inferred ecophysiology of microorganisms with the potential for dissimilatory sulfate/sulfite reduction, FEMS Microbiol. Rev. 47 (2023) fuad058, https://doi.org/10.1093/femsre/fuad058 . [40] M.K.D. Dueholm, K.S. Andersen, A.K.C. Korntved, et al., MiDAS 5: global diversity of bacteria and archaea in anaerobic digesters, Nat. Commun. 15 (2024) 5361, https://doi.org/10.1038/s41467-024-49641-y . [41] APHA/AWWA, 1995. Standard Methods for the Examination of Water and Wastewater. Port City Press, Balt. Bengtsson, S., Hallquist, J., Werk. [42] J.R. Pereira, D. Araújo, A.C. Marques, L.A. Neves, C. Grandfils, C. Sevrin, V. D. Alves, E. Fortunato, M.A.M. Reis, F. Freitas, Demonstration of the adhesive properties of the medium-chain-length polyhydroxyalkanoate produced by Pseudomonas chlororaphis subsp. aurantiaca from glycerol, Int J. Biol. Macromol. 1 (122) (2019) 1144 – 1151, https://doi.org/10.1016/j.ijbiomac.2018.09.064 . Epub 2018 Sep 13. PMID: 30219510. [43] Y. Zheng, C. Hu, X. Wang, Z. Wu, Physics-informed recurrent neural network modeling for predictive control of nonlinear processes, J. Process Control 128 (2023) 103005, https://doi.org/10.1016/j.jprocont.2023.103005 . [44] Mohd Zafar, Shashi Kumar, Surendra Kumar, Amit K. Dhiman, Artificial intelligence based modeling and optimization of poly(3-hydroxybutyrate-co-3-
hydroxyvalerate) production process by using Azohydromonas lata MTCC 2311 from cane molasses supplemented with volatile fatty acids: a genetic algorithm paradigm, Bioresour. Technol. 104 (2012) 631 – 641, https://doi.org/10.1016/j. biortech.2011.10.024 . [45] P. Lhamo, B. Mahanty, S.K. Behera, Optimization of biomass and polyhydroxyalkanoate production by Cupriavidus necator using response surface methodology and genetic algorithm optimized artificial neural network, Biomass.. Conv. Bioref. 14 (2024) 20053 – 20068, https://doi.org/10.1007/s13399-023- 04043-w . [46] S. Yang, W. Fahey, B. Truccollo, J. Browning, R. Kamyar, H. Cao, Hybrid modeling of fed-batch cell culture using physics-informed neural network, Ind. Eng. Chem. Res. (2024), https://doi.org/10.1021/acs.iecr.4c01459 . [47] P. Jul-Rasmussen, M. Kumar, J. Pinto, R. Oliveira, X. Liang, J.K. Huusom, Incorporating first-principles information into hybrid modeling structures: Comparing hybrid semi-parametric models with Physics-Informed Recurrent Neural Networks, Comput. Chem. Eng. (2025) 109119, https://doi.org/10.1016/j. compchemeng.2025.109119 . [48] F. Moayedi, A. Chandrasekar, S. Rasmussen, S. Sarna, B. Corbett, P. Mhaskar, Physics-informed neural networks for process systems: handling plant-model mismatch, Ind. Eng. Chem. Res. 63 (31) (2024) 13650 – 13659, https://doi.org/ 10.1021/acs.iecr.4c00690 . [49] Monesh kumar Thirugnanasambandam, et al., "A Physics-Informed Neural Network (PINN) framework for generic bioreactor modelling, Comput. Chem. Eng. (2025) 109354, https://doi.org/10.1016/j.compchemeng.2025.109354 . [50] M.F. Luna, A.M. Ochsner, V. Amstutz, D. von Blarer, M. Sokolov, P. Arosio, M. Zinn, Modeling of continuous PHA production by a hybrid approach based on first principles and machine learning, Processes 9 (2021) 1560, https://doi.org/ 10.3390/pr9091560 . [51] J. Peres, R. Oliveira, L.S. Serafim, P. Lemos, M.A. Reis, S. Feyo de Azevedo, Hybrid modelling of a PHA production process using modular neural networks, Editor(s): A. Barbosa-P ´ ovoa, H. Matos, in: Computer Aided Chemical Engineering, 18, Elsevier, 2004, pp. 733 – 738, https://doi.org/10.1016/S1570-7946(04)80188-3 . [52] S.J. Pan, Q. Yang, "A survey on transfer learning, IEEE Trans. Knowl. Data Eng. 22 (10) (Oct. 2010) 1345 – 1359, https://doi.org/10.1109/TKDE.2009.191 .
13

> [!info] Related Concept
> See also: [[Bio-Process#31-historical-microbiome-data-set-<a-id="3-1-historical-microbiome-data-set"></a>|3.1. Historical microbiome data set <a id="3-1-historical-microbiome-data-set"></a>]] in Bio-Process

> [!info] Related Concept
> See also: [[Bio-Process#31-historical-microbiome-data-set-<a-id="3-1-historical-microbiome-data-set"></a>|3.1. Historical microbiome data set <a id="3-1-historical-microbiome-data-set"></a>]] in Bio-Process

> [!info] Related Concept
> See also: [[Bio-Process#31-historical-microbiome-data-set-<a-id="3-1-historical-microbiome-data-set"></a>|3.1. Historical microbiome data set <a id="3-1-historical-microbiome-data-set"></a>]] in Bio-Process

> [!info] Related Concept
> See also: [[Bio-Process#31-historical-microbiome-data-set-<a-id="3-1-historical-microbiome-data-set"></a>|3.1. Historical microbiome data set <a id="3-1-historical-microbiome-data-set"></a>]] in Bio-Process

> [!info] Related Concept
> See also: [[Bio-Process#31-historical-microbiome-data-set-<a-id="3-1-historical-microbiome-data-set"></a>|3.1. Historical microbiome data set <a id="3-1-historical-microbiome-data-set"></a>]] in Bio-Process

> [!info] Related Concept
> See also: [[Bio-Process#31-historical-microbiome-data-set-<a-id="3-1-historical-microbiome-data-set"></a>|3.1. Historical microbiome data set <a id="3-1-historical-microbiome-data-set"></a>]] in Bio-Process

> [!info] Related Concept
> See also: [[Bio-Process#31-historical-microbiome-data-set-<a-id="3-1-historical-microbiome-data-set"></a>|3.1. Historical microbiome data set <a id="3-1-historical-microbiome-data-set"></a>]] in Bio-Process

> [!info] Related Concept
> See also: [[Bio-Process#31-historical-microbiome-data-set-<a-id="3-1-historical-microbiome-data-set"></a>|3.1. Historical microbiome data set <a id="3-1-historical-microbiome-data-set"></a>]] in Bio-Process

> [!info] Related Concept
> See also: [[Bio-Process#26-implementation-<a-id="2-6-implementation"></a>|2.6. Implementation <a id="2-6-implementation"></a>]] in Bio-Process

> [!info] Related Concept
> See also: [[Bio-Process#26-implementation-<a-id="2-6-implementation"></a>|2.6. Implementation <a id="2-6-implementation"></a>]] in Bio-Process

> [!info] Related Concept
> See also: [[Bio-Process#26-implementation-<a-id="2-6-implementation"></a>|2.6. Implementation <a id="2-6-implementation"></a>]] in Bio-Process

> [!info] Related Concept
> See also: [[Bio-Process#26-implementation-<a-id="2-6-implementation"></a>|2.6. Implementation <a id="2-6-implementation"></a>]] in Bio-Process

> [!info] Related Concept
> See also: [[Bio-Process#31-historical-microbiome-data-set-<a-id="3-1-historical-microbiome-data-set"></a>|3.1. Historical microbiome data set <a id="3-1-historical-microbiome-data-set"></a>]] in Bio-Process

> [!info] Related Concept
> See also: [[Bio-Process#31-historical-microbiome-data-set-<a-id="3-1-historical-microbiome-data-set"></a>|3.1. Historical microbiome data set <a id="3-1-historical-microbiome-data-set"></a>]] in Bio-Process

> [!info] Related Concept
> See also: [[Bio-Process#31-historical-microbiome-data-set-<a-id="3-1-historical-microbiome-data-set"></a>|3.1. Historical microbiome data set <a id="3-1-historical-microbiome-data-set"></a>]] in Bio-Process

> [!info] Related Concept
> See also: [[Bio-Process#31-historical-microbiome-data-set-<a-id="3-1-historical-microbiome-data-set"></a>|3.1. Historical microbiome data set <a id="3-1-historical-microbiome-data-set"></a>]] in Bio-Process

> [!info] Related Concept
> See also: [[Bio-Process#34-process-control-experiment-<a-id="3-4-process-control-experiment"></a>|3.4. Process control experiment <a id="3-4-process-control-experiment"></a>]] in Bio-Process

> [!info] Related Concept
> See also: [[Bio-Process#34-process-control-experiment-<a-id="3-4-process-control-experiment"></a>|3.4. Process control experiment <a id="3-4-process-control-experiment"></a>]] in Bio-Process

> [!info] Related Concept
> See also: [[Bio-Process#34-process-control-experiment-<a-id="3-4-process-control-experiment"></a>|3.4. Process control experiment <a id="3-4-process-control-experiment"></a>]] in Bio-Process

> [!info] Related Concept
> See also: [[Bio-Process#34-process-control-experiment-<a-id="3-4-process-control-experiment"></a>|3.4. Process control experiment <a id="3-4-process-control-experiment"></a>]] in Bio-Process

> [!info] Related Concept
> See also: [[reactor modelling#credit-authorship-contribution-statement-<a-id="credit-authorship-contribution-statement"></a>|CRediT authorship contribution statement <a id="credit-authorship-contribution-statement"></a>]] in [[reactor modelling]]

> [!info] Related Concept
> See also: [[reactor modelling#credit-authorship-contribution-statement-<a-id="credit-authorship-contribution-statement"></a>|CRediT authorship contribution statement <a id="credit-authorship-contribution-statement"></a>]] in [[reactor modelling]]

> [!info] Related Concept
> See also: [[reactor modelling#credit-authorship-contribution-statement-<a-id="credit-authorship-contribution-statement"></a>|CRediT authorship contribution statement <a id="credit-authorship-contribution-statement"></a>]] in [[reactor modelling]]

> [!info] Related Concept
> See also: [[reactor modelling#credit-authorship-contribution-statement-<a-id="credit-authorship-contribution-statement"></a>|CRediT authorship contribution statement <a id="credit-authorship-contribution-statement"></a>]] in [[reactor modelling]]