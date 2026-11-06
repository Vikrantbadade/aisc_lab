# Bidirectional Associative Memory (BAM) for English-Hindi Word Pairs

## Aim
To design and implement a Bidirectional Associative Memory (BAM) that learns associations between English words and their Hindi translations and recalls the correct translation in both directions.

## Theory
A Bidirectional Associative Memory (BAM) is a hetero-associative neural network with two layers. It stores pairs of patterns in one weight matrix and recalls in both directions: the Hindi pattern from an English pattern using `W`, and the English pattern from a Hindi pattern using `Wᵀ`. The two layers pass activity back and forth until they settle on a stable pair.

### Training: Hebbian Rule
The BAM weight matrix is constructed using:

`W = Σ x(p)ᵀ y(p)`

### Word Encoding
Words are written in lowercase. Hindi translations are represented in Roman script. Each letter position has 26 binary neurons, with the neuron corresponding to the letter set to 1.

- English words use 5 × 26 = 130 neurons.
- Hindi words use 6 × 26 = 156 neurons.
- Shorter words leave the remaining positions as zero.

### Recall
Neuron sums are converted back into letters using a winner-take-all choice in each letter position. A position is kept only when its support is at least half of the strongest support in that layer. This prevents weak cross-talk from adding extra letters.

### Stored Word Pairs

| English | Hindi (Roman script) |
|---|---|
| dog | kutta |
| cat | billi |
| sun | suraj |
| moon | chand |
| tree | ped |
| book | kitab |
| water | paani |
| star | tara |

## Evaluation
The practical evaluates:
1. Forward recall: English to Hindi.
2. Reverse recall: Hindi to English.
3. Recall for similar-looking or alternate spellings.
4. Recall accuracy after randomly flipping input bits, using 100 trials per pair.
5. A graph of recall accuracy against the number of flipped bits and a visualization of the BAM weight matrix.

## Result
The supplied practical reports 8/8 correct English-to-Hindi recalls and 8/8 correct Hindi-to-English recalls. With up to 12 randomly flipped input bits, recall accuracy was 86.6% in the forward direction and 92.1% in the reverse direction.

Similar or misspelled inputs do not always produce the intended association because the network matches them against stored letter patterns. The practical demonstrates recall from noisy or incomplete inputs and shows that accuracy depends on overlap between stored patterns.

## Requirements
Install the required libraries using:

`pip install numpy matplotlib`
