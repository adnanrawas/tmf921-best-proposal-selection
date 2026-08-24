# O-RAN Agentic Resource Allocation

This work investigates intelligent resource allocation using an agent-based model
in the Distributed Unit (DU) and the Centralized Unit (CU)
within O-RAN architectures. A LangGraph-based control layer is
integrated into the SMO to support human-in-the-loop decision-making.

## Architecture

![Architecture](images/architectureV2.gif)

### Multi-Agent Consensus Workflow

The following workflow illustrates the multi-agent ranking, consensus, negotiation, and slice Proposal recommendation .

![Multi-Agent Consensus Workflow](images/multi_agent_consensus_workflow.gif)

### Multi-Agent Consensus Sequence

The following sequence diagram illustrates the interactions and message flow between the agents during the consensus process.

![Multi-Agent Consensus Sequence Diagram](images/final_high_level_sequence_diagram.png)

## 📂 Project Structure

```text
oran-agentic-resource-allocation/
├── agents/               # Autonomous agent logic for resource allocation tasks
├── api/                  # REST API endpoints and logic (Flask)
├── frontend/             # Frontend
├── images/               # Static assets, diagrams, and visual resources
├── init.sql              # Initial SQL script for database setup
├── llm/                  # Large Language Model integration
├── mock/                 # Mock data and testing
├── postgres/             # PostgreSQL database configurations and scripts
├── smo/                  # System management and orchestration
├── .env                  # Environment variables 
├── .gitignore            
├── docker-compose.yml    # Docker container orchestration configuration
└── README.md             
```

## NSGA-II Baseline for Multi-Objective Optimization

This project uses the Non-Dominated Sorting Genetic Algorithm II (NSGA-II) as a baseline method to solve a multi-objective resource allocation problem in O-RAN network slicing.

The optimization jointly considers four conflicting objectives:

 maximize total throughput
- minimize total latency
- minimize total cost
- minimize total energy consumption

Each candidate solution represents slice-level resource allocations for:
- bandwidth
- compute
- power
- storage

The considered slice types are:
- eMBB: Enhanced Mobile Broadband, focused on high data-rate services
- URLLC: Ultra-Reliable Low-Latency Communications, focused on delay-sensitive and highly reliable services
- mMTC: Massive Machine Type Communications, focused on large-scale IoT connectivity

### Implementation

This project uses [PyGAD](https://pygad.readthedocs.io/) version `3.2.0` to implement NSGA-II for multi-objective optimization.
- PyGAD documentation: [pygad.readthedocs.io](https://pygad.readthedocs.io/)
- PyGAD repository: [ahmedfgad/GeneticAlgorithmPython](https://github.com/ahmedfgad/GeneticAlgorithmPython)
- PyGAD 3.2.0 release notes: [PyGAD-3.2.0](https://pygad.readthedocs.io/en/latest/pygad_more.html#save-solutions)

!-- ## NSGA-II 

The following figures show preliminary NSGA-II results based on global resource limits and phase KPI constraints. User-specific requirements are not yet included in the optimization loop.
<!-- ![Global Resource Limits](images/Global_Resource_Limit.jpg)
![SLA Constraints](images/SLA_Constraints.jpg) 
![Best Resources by Slice](images/Best_Resources_by Slice.jpg)
![KPIs of Best Solution](images/KPIs_of_Best_Solution)
![Front 0 Pareto Solutionsn](images/Front_0_Pareto_Solutions_Slice_KPIs.jpg)
 Full JSON output: [nsga2_result.json](results/baseline/nsga2_result.json)
 PowerPoint presentation: [NSGA-II_Baseline.pptx](slides/NSGA-II_Baseline.pptx) -->

- [Global Resource Limits](images/Global_Resource_Limit.jpg)
- [SLA Constraints](images/SLA_Constraints.jpg) 
- [Best Resources by Slice](images/Best_Resources_by_Slice.jpg)
- [KPIs of Best Solution](images/KPIs_of_Best_Solution.jpg)
- [Front 0 Pareto Solutionsn](images/Front_0_Pareto_Solutions_Slice_KPIs.jpg)
- Full JSON output: [nsga2_result.json](results/baseline/nsga2_result.json)
<!-- - PowerPoint presentation: [NSGA-II_Baseline.pptx](slides/NSGA-II_Baseline.pptx) -->

## Multi-Criteria Decision Service
Run the TOPSIS-based ranking and VIKOR service from the host terminal:
```bash
curl -sS -X POST "http://localhost:9000/topsis/save-jsons" \
  -H "Content-Type: application/json" \
  -d '{}'

curl -sS -X POST "http://localhost:9000/vikor/save-jsons" \
  -H "Content-Type: application/json" \
  -d '{}'
```
## Experiments and Baselines

The following experiments compare deterministic ranking methods, reasoning-based selection, multi-agent consensus, and counterproposal-based negotiation.

| ID | Input | Decision method | Initial proposal | Counterproposal |
|---|---|---|---|---|
| B1 | Feasible offers | SAW | Yes | No |
| B2 | Feasible offers | TOPSIS | Yes | No |
| B3 | Feasible offers | VIKOR | Yes | No |
| A1 | Raw feasible offers (no rankings) | Multi-agent consensus | Yes | No |
| A2 | TOPSIS + VIKOR rankings | One reasoning agent | Yes | No |
| A3 | TOPSIS + VIKOR rankings | Multi-agent consensus | Yes | No |
| Full system | TOPSIS + VIKOR rankings | Multi-agent consensus | Yes | Yes |

### Comparison Goals

- A1 vs A3: effect of providing TOPSIS and VIKOR rankings to consensus agents.
- A2 vs A3: effect of multi-agent consensus compared with one reasoning agent.
- B1–B3 vs A3: comparison with deterministic ranking baselines.
- A3 vs Full system: effect of counterproposals on the final selection.
## Planned Evaluation Metrics
The weighted-utility concept is adapted from the iMnet framework
(Priya & Malhotra, 2022).

$$
U(\text{offer}) = w_T T + w_L \frac{1}{L} + w_C \frac{1}{C} + w_E \frac{1}{E}
$$

Where:

- \(T\): throughput; higher is better.
- \(L\): latency; lower is better.
- \(C\): cost; lower is better.
- \(E\): energy; lower is better.
- \(w_T, w_L, w_C, w_E\): intent KPI weights.


This utility function aggregates throughput, latency, cost, and energy using intent-defined weights to quantify the overall multi-criteria performance of a selected resource-allocation offer.

## References
Priya, B., & Malhotra, J. (2022). *iMnet: Intelligent RAT selection
framework for 5G-enabled IoMT network*. *Wireless Personal
Communications, 129*(2), 911–932.
https://doi.org/10.1007/s11277-022-10163-9
<!--
## Scenario 1 – DU Resource Allocation
![Scenario 1](images/seanario1.jpg)
### The evaluation of the agent's results is performed using the following

resource allocation and RAN performance KPIs:

- RRC Connection Establishment Success Rate
- Physical Resource Block (PRB) Usage
- OR.CellU.ActDeactMacCeScellDeact (SCell activation/deactivation counter)
- MCS(Modulation and Coding Scheme Key)
-->
