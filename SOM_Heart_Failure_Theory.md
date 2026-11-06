# Kohonen Self-Organizing Map (SOM) for Heart Failure Patient Clustering

## Aim
To apply a Kohonen Self-Organizing Map (SOM) to cluster heart failure patients based on demographic, lifestyle and clinical features, and interpret the clusters in terms of medical risk profiles.

## Theory
A Self-Organizing Map (SOM), also called a Kohonen Self-Organizing Feature Map (KSOFM), is an unsupervised neural network. It maps high-dimensional input data onto a low-dimensional grid, usually two-dimensional, while preserving topological relationships. Nearby neurons represent similar input patterns.

Each neuron in the grid has a weight vector with the same number of elements as the input feature vector.

### Best Matching Unit (BMU)
For each input vector, the SOM calculates the distance between the input and every neuron's weight vector. The neuron with the smallest distance is called the Best Matching Unit (BMU) or winning neuron.

### Training
1. Prepare the patient dataset and handle missing values.
2. Normalize numerical features.
3. Define a SOM grid, such as 10×10 neurons.
4. Initialize neuron weights.
5. Find the BMU for each patient record.
6. Update the BMU and its neighboring neurons to move their weights closer to the input.
7. Repeat the process until the map is organized.

### Clustering and Interpretation
After training, each patient is assigned to the BMU. Patients assigned to the same neuron are grouped together. Cluster quality can be assessed using the Silhouette Score or Davies-Bouldin Index.

The `DEATH_EVENT` column can be compared with the resulting clusters to examine whether the map separates groups with different observed death-event rates. This comparison is for interpretation; `DEATH_EVENT` is not used as an input feature during SOM training.

### Visualization
The program plots patient BMU positions on the SOM grid. The points are colored by `DEATH_EVENT` to help interpret the distribution of the observed outcome across clusters.

## Result
The SOM groups heart failure patient records according to similarities in their clinical and demographic features. The program reports occupied clusters, cluster sizes, death-event rates and the Silhouette Score when it can be calculated.

## Dataset and Requirements
Place `heart_failure_clinical_records_dataset.csv` in the same directory as the Python file. The CSV must contain a `DEATH_EVENT` column and the heart failure patient features.

Install the required libraries using:

`pip install numpy pandas matplotlib scikit-learn`

The dataset is not included in the supplied practical PDF, so it must be obtained separately.
