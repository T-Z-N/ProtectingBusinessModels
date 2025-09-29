## Overview

Business models are critical but vulnerable assets in today's innovation-driven economy. While practitioners employ diverse defensive tactics and scholars have produced valuable research on specific protection strategies, this knowledge remains fragmented. Our research addresses this gap by developing the first comprehensive taxonomy of business model protection mechanisms.

## Key Contributions

- **15 Top-Level Protection Strategies**: A validated framework identifying the core strategies for business model protection
- **Hierarchical Taxonomy**: A multi-level structure showing how 176 initial mechanisms relate through composition, abstraction, and means-end relationships
- **Interactive Visualization Tools**: Custom D3.js tools for exploring the taxonomy and understanding mechanism relationships
- **Replicable Methodology**: A novel approach combining expert workshops, computational text analysis, and structured validation

## Repository Contents

### 📊 Interactive Visualizations

Refresh the page, if the visualizations do not load.

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
- `Initial_set_of_mechanisms.md` - The 176 raw mechanisms extracted from expert workshops
- `Abstract_new_mechanisms.md` - The 26 abstracted concepts forming the taxonomy nodes
- `unvalidatedHiearchy.json` - The preliminary hierarchical structure before expert validation
- `validatedHiearchy.json` - The complete validated hierarchical structure

#### Analysis Scripts
- `embedding_analysis.py` - Computational text analysis using sentence transformers
- `graph_construction.py` - Network analysis and clique detection algorithms
- `taxonomy_builder.py` - Hierarchy construction and relationship classification

### 📚 Documentation

- `validation_protocol.md` - Expert validation workshop procedures
- `presentation.text` - Placeholder for the validation presentation file. Did not disclosed due to peer-review process.

## Using the Tools

### Clique Analysis Tool
```bash
# Open the interactive clique tool
open [clique_tool](https://t-z-n.github.io/Semantic-Similarity-Visualizer/)

# Adjust the similarity threshold using the slider
# Observe clique formation at different threshold levels
# Use for identifying semantic clusters in the initial set of mechanisms
```

### Taxonomy Browser
```bash
# Explore the final validated taxonomy
open [taxonomy_visualization](https://t-z-n.github.io/PBM_Visualization/)

# Navigate through the hierarchical structure
# Click on nodes to explore relationships
# Use legend to understand relationship types
```

