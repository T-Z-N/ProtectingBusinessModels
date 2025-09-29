## Overview

Business models are critical but vulnerable assets in today's innovation-driven economy. While practitioners employ diverse defensive tactics and scholars have produced valuable research on specific protection strategies, this knowledge remains fragmented. Our research addresses this gap by developing the first comprehensive taxonomy of business model protection mechanisms.

## Key Contributions

- **15 Top-Level Protection Strategies**: A validated framework identifying the core strategies for business model protection
- **Hierarchical Taxonomy**: A multi-level structure showing how 176 initial mechanisms relate through composition, abstraction, and means-end relationships
- **Interactive Visualization Tools**: Custom D3.js tools for exploring the taxonomy and understanding mechanism relationships
- **Replicable Methodology**: A novel approach combining expert workshops, computational text analysis, and structured validation

## Repository Contents

### 📊 Interactive Visualizations

#### Clique Analysis Tool
- **File**: [clique_tool](https://t-z-n.github.io/Semantic-Similarity-Visualizer/)
- **Purpose**: Interactive graph analysis tool used during our methodology
- **Features**:
  - Dynamic threshold adjustment for similarity analysis
  - Automatic clique detection (k=3 and k=4)
  - Real-time visualization of mechanism relationships
  - Used for identifying clusters of semantically related mechanisms

#### Final Taxonomy Browser
- **Link**: [taxonomy_visualization](https://t-z-n.github.io/PBM_Visualization/)
- **Purpose**: Interactive exploration of the validated taxonomy
- **Features**:
  - Hierarchical structure navigation
  - Relationship type visualization (Composition/Aggregation, Abstraction/Specification, Means/End)
  - Complete taxonomy with all 15 top-level strategies

### 📋 Data and Results

#### Mechanism Sets
- `initial_mechanisms.json` - The 176 raw mechanisms extracted from expert workshops
- `final_concepts.json` - The 26 abstracted concepts forming the taxonomy nodes
- `validated_taxonomy.json` - The complete validated hierarchical structure

#### Analysis Scripts
- `embedding_analysis.py` - Computational text analysis using sentence transformers
- `graph_construction.py` - Network analysis and clique detection algorithms
- `taxonomy_builder.py` - Hierarchy construction and relationship classification

### 📚 Documentation

- `methodology_overview.md` - Detailed description of our multi-stage methodology
- `validation_protocol.md` - Expert validation workshop procedures
- `relationship_types.md` - Explanation of the three fundamental relationship types

## Methodology Summary

Our research employed a four-stage methodology:

1. **Expert Knowledge Elicitation**: Multi-stakeholder workshop (N=25) using World Café methodology
2. **Data Structuring**: Transcription, translation, and assertion-mechanism extraction (176 mechanisms)
3. **Computational Analysis**: Semantic similarity analysis, graph construction, and iterative clique-based abstraction
4. **Expert Validation**: Structured validation workshop with domain experts (N=4)

## The 15 Top-Level Protection Strategies

1. **Unique Differentiating Features**
2. **Structural Sophistication & Complexity**
3. **Brand Equity**
4. **Customer Loyalty**
5. **Strategic Relationship Advantage**
6. **Business Model Lifecycle Management**
7. **Comprehensive Legal/IP Strategy & Enforcement**
8. **Dynamic Capability & Adaptability**
9. **Securing Human Capital Advantage**
10. **Knowledge and Insight Advantage**
11. **Data Dominance & Control**
12. **Specialize and Dominate Strategy**
13. **Ecosystem Strategy & Positioning**
14. **Execution Distinction**
15. **Confidentiality & Information Control**

## Using the Tools

### Clique Analysis Tool
```bash
# Open the interactive clique tool
open clique_tool.html

# Adjust the similarity threshold using the slider
# Observe clique formation at different threshold levels
# Use for identifying semantic clusters in your own data
```

### Taxonomy Browser
```bash
# Explore the final validated taxonomy
open taxonomy_visualization.html

# Navigate through the hierarchical structure
# Click on nodes to explore relationships
# Use legend to understand relationship types
```

## Theoretical Framework

Our taxonomy reveals business model protection as a **dynamic system of interconnected actions** rather than a static portfolio of assets. The prevalence of Means-End relationships throughout the taxonomy demonstrates that protection mechanisms should be understood by what they do, not just what they are.

### Relationship Types

- **Composition/Aggregation (C/A)**: Child represents a part of the parent
- **Abstraction/Specification (A/S)**: Child is a type or instance of the parent category  
- **Means/End (M/E)**: Child serves as a method for achieving the parent objective

## Practical Applications

### For Managers
- **Strategic Diagnosis**: Map current protection activities onto the framework
- **Gap Analysis**: Identify overlooked protection mechanisms
- **Portfolio Planning**: Understand how different strategies reinforce each other

### For Researchers
- **Theoretical Foundation**: Structured vocabulary for business model protection research
- **Comparative Studies**: Framework for analyzing protection strategies across contexts
- **Future Research**: Starting point for deeper investigation of specific mechanisms

## Limitations and Future Work

- **Context**: Based on European manufacturing-focused workshop
- **Generalizability**: Requires validation across diverse industries and cultures
- **Granularity**: Future work could explore more detailed relationship classifications
- **Practitioner Validation**: Additional validation with industry practitioners needed

## Citation

If you use this framework or tools in your research, please cite:

```bibtex
@article{tuzun2024architecture,
  title={The Architecture of Defense: A Systemic Framework for Protecting Business Models},
  author={},
  journal={[Journal Name]},
  year={2024}
}
```

## Contact

For questions about this research or collaboration opportunities:

XXXXXXX
