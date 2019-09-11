# comments from JOel 190415

Section 2.3. There are a few strange turns of phrase here ("intrigues"?). You might want to read through this quickly (out loud!) and edit to make it more fluent.

√ line 155. Your account of my comment is good.

√ line 197. We should be careful to circumscribe our novelty claim for [27].

√ line 199. Would be good to remind the reader that this is the Khatri–Rao product.

~ line 208. I think it's a bit misleading to say that the computation scales as I^N. This is true when applying the map to a full tensor, whereas we typically think about sketching much simpler objects (at much lower cost). Might be good to quantify the cost of applying the maps to a rank-one tensor?

Table 1 (and elsewhere). I generally prefer to set figures, tables, and algorithms at the top of a page (using the [t] flag).

√ Section 4. This title isn't accurate. Maybe "Algorithms for Tucker approximation"?

√ line 217 (and elsewhere). I don't like the term "statistical guarantees." This suggests that some probabilistic data model. I prefer just "guarantees" or maybe "probabilistic guarantees" to emphasize that the results aren't conditional.

! line 217 (and elsewhere). There are some broken xrefs.

? line 277–280. I still don't understand this heuristic computation. It requires more explanation.

√ line 292. You could just cite the SISC paper as evidence of this point in the matrix setting, e.g., by referring to the figures on rank truncation.

√ Section 5. Please do not call the guarantees "statistical", for the reasons mentioned above. They're simply guarantees.

√ line 345. Reviewers have complained about the term "adapts." The word "exploits" is a bit closer to what we mean. It would be even better to explain that the method works best for tensors where the unfoldings have spectral decay, and this is what the bound says in words.

√ line 361. The square-root on the right-hand side does not belong!

√ line 362. The conditional theorem (5.3) looks okay to me, but I don't like the corollary (5.1) so much. It takes up a lot of space for something that follows from a substitution. Just add a line to say that the second term on the right-hand side of line 361 is controlled by the results in Thms. 5.1, 5.2. The rest of the commentary is still valid.

! Section 5.3. When stating a theorem but deferring (or omitting) the proof, you need an explicit cross-reference (or citation) to the proof adjacent to the theorem. You also need xrefs in Sec. 5.3 so the reader can find the detailed arguments.

! MU: change terminology as indicated in numerical experiments

! Figure 1. The figures are easier to read than before, modulo the previous remark. You might want to compress the title of the figure and set it in italics (or something). It wouldn't hurt to emphasize that the tensors have three modes. (You have to infer this from the rank triple!) Moreover, you're also reporting a per-mode compression factor, rather than the total compression (delta_1^3). The latter is much more impressive...

line 461. I don't understand how you are relating our results to the HOOI error, unless you're using what I call relative error. Please clarify!!!

! Figure 2. Some of the panels have only one labeled tick mark. You need at least two. Also, you might compress the title of the figure.

line 469. There's no convergence here, nor an asymptote. I would say that the data series exhibit a similar decay profile.

! page 18. Every figure needs a caption and an explicit reference to the figure in the body of the paper.

# Some comments from Tammy we could address further

* I don’t see that this covers how to choose the rank to preserve a specific error. That’s often important in applications.

# Name

Direct Tucker Tensor Sketch ? Ugh

In figures:

[OB18]
[SGLTU19] / proposed

Figure 3: labels can occupy the sixth square; remove them from overlay
Harmonize "one pass" vs "1-pass", esp figure labels
All figures must make clear which algos are proposed / new

# Comments from Joel 190307

todos for Yang:
* delete gaussian maps from comparison after confirming universality of TRP
* note in paper that HOOI is more expensive than necessary: "I actually recommend against using HOOI these days. It turns out that this buys little improvement as compared to HOSVD and especially as compared to a newer technique called sequentially-truncated HOSVD (ST-HOSVD). In [6], we talk about it and there are some results that show that HOOI doesn’t yield any improvements.""
* y axes are unreadable
  * subtract HOOI error (1) and put it on a log scale
  * axis should not be in scientific notation
* plot error as a function of runtime for fixed storage cost
  * scalings, not absolutes, are important: so make sure plot is wide enough to see scaling
* visualizations of tensors
  * slices
  * movies

todos for madeleine:
* reread email from Tammy
* increase text describing how we answer joel's high level bullets in experiments
* communication complexity is main bottleneck in HOOI / HOSVD; hit this point harder
* use for compression: ST-HOSVD or tensor train might be great; but we don't know how to compute them in one pass.

questions for later:
* how to choose rank truncation? definitely same rank in each dimension is stupid for real data
* a posteriori bound

line 64. "In contrast" doesn't have a clear ßprecedent.
line 68. "optimization process (ALS)" isn't clear. I think you're saying that the expensive computations only take place on the small-ish core sketch.
line 70. The contrast with [21] might be relegated to the related work section. It's also not necessary to tangle up the explanation of our algorithm with a description of [21]. We can explain our method and then place [21] in contrast.
line 77. We're treating the tensor as a *multilinear* operator. The sketch identifies a low-dimensional subspace *for each input argument* that captures the action of the operator. The reconstruction produces a low-Tucker-rank multilinear operator with the same action on this low-dimensional tensor product space.
line 111. The usual style is $i$th and $j$th, without hyphens or superscripts, but write $(i, j)$-th for a complicated ordinal.
line 136. Don't use logical symbols in text. Write out "if and only if." In fact, logical symbols are rarely better than their text equivalents.
line 107. I prefer to put the intro in its own section, and start a new top-level section for technical material. Secs. 1.1–1.3 are all "Background and Related Work."
line 153. Tammy indicated that she doesn't know if low-rank Tucker approximation is hard, and I think Jiawang said something similar. We should be careful about what we claim here.
line 164. "Leading left eigenvectors"? This term needs to be defined. Moreover, I'm not sure that this is what we really mean.
line 166. Didn't Tammy trash HOOI?
line 168. (I can see that you haven't made it this far, so I'll skip line edits except for technical concerns.)

line 227. Haven't defined the term "test matrix." Maybe just say "dimension reduction maps."
line 239. It's *often* smaller than the full tensor, but it depends on the parameter choices.
-> Alg. 2.1. I prefer to use the [t] specifier on floats.
-> Alg. 2.1. Do we want to combine the sketch constructor and the matrix sketch?
line 246. We are just proposing to *use* TRP, but it has been developed elsewhere.
line 255. More logical symbols in text!
line 290. The derivation in this section is still a bit confusing.

-> line 303. One of the innovations in the SISC revision is to recognize that rank truncation is essential to make the low-rank approximation fully reliable. The numerics there suggested that k > 4r was a good rule of thumb. By "reliable", I mean that all of the computed singular values and vectors of the matrix agree with those of the input data.

line 317. We should present the storage / arithmetic costs of our method without reference to [21]. It's useful to make a comparison, but this should be separated from our own analysis.

Tables 1–2. Instead of "Proposed", we should be clear about which of our algorithms we're referring to.

line 336. We put the proof in the supplement because it's similar in spirit to the SISC paper. But I think the students had a few nice ideas (e.g., the "martingale" decomposition of the algorithm) that might be worth explaining in the main text. Formal statements may not be necessary, but it would be good to indicate where the difficulty / novelty of the analysis lies.

Theorems 3.1/3.2. We should be more precise about what the theorems are about. Give them names like "Error bound: One-pass approximation".

line 361. This conditional result is a bit ridiculous. I'd seriously consider removing it and the corollary. At the very least, we might want to reduce the amount of space we spend on this. Or we could give a more discursive presentation in the text, rather than labeling it as a "theorem" with a hypothesis that is probably false.

line 390. Is low-rank Tucker approximation actually computationally hard?

line 394. We should make sure we're crystal clear about what algorithm(s) from [21] we're comparing with, as well as the exact method that we are proposing to use.

line 401. I prefer to call this the "normalized" error, rather than the "relative" error. The former scales the error so it should usually be less than one. The second compares the error with the "optimum" error: ||X - hat{X}|| / ||X - HOOI(X)|| - 1.You might consider whether you actually want the latter.

Figures 1–2, 4. I find the vertical scale here very confusing. I think my issue is that the decimals and exponent make the numbers unreadable. At the very least, the tick locations and labeling need to be revisited. In contrast, Figure 3 is just fine.

Figure 2. The series are too hard to tell apart; don't use the same marker for two different things. Also: once we've done a "universality" experiment (i.e., Figure 1), it's reasonable to omit further comparisons with Gaussians in favor of the TRP. Indeed, the performance appears similar, even in the "real data" examples.

For SISC, we did some other experiments to try to explain why rank truncation is useful. We also tried to use a posteriori information to decide where to truncate the rank. These things are also possible in the tensor context.

Sec. 4.2. These data sets aren't really that large and, in particular, they don't qualify as things that won't fit in memory. We should be careful about making this claim. Also: Why quote the size of the video data, but not the other datasets?

line 490. Surely, these matrices fit into RAM. They're only a few hundred Megabytes.

line 493. When we try three target ranks, do we change the sketch size? We could certainly fix the sketch size and compute approximations of various ranks, using an a posteriori error estimator to try to decide which is best.

For the data matrices, the modes have different dimensions, so it doesn't make sense to talk about the rank as a proportion of the (common) dimension I of the index sets. This is a confusing aspect of Figure 4, and it needs to be clarified.

The explanations of the experiments could use work. The text can be qualitative, but somewhere you have to say exactly what we're doing. For example, I don't understand how we are applying k-means in line 505. It's also not clear why we make some parameter selections, e.g., three clusters or why we select specific choices of rank.

The video example obviously lends itself well to visualization. Since there are only three classes, the diagram could be improved. You could have a thin bar that changes color to reflect the class, and you could place exemplar frames in a line underneath with some kind of arrow to connect each frame to the associated point in the thin bar.

The combustion data can probably be visualized as well. My colleague may even have scripts for doing so. This would be more dramatic than just making charts. Also: if the tensor really is low rank, you can use one variable to predict others (e.g., pressure predicts CO2 concentration), which is a sort of transfer learning. One nice presentation is just to show slices of the original data and how the reconstructions compare. We could also try to compare "singular vectors".

Tammy has some interesting ways of visualizing tensors, so you might want to have a look at some of her slides. For a three-dimensional tensor (space x space x time), for instance, you can represent the spatial dimensions as 2d images alongside a time series. (This is roughly what we did for the sea-surface temperature data in the SISC paper.)

# Usage scenarios

Goal: compression

Limitations of data access model:
* Streaming / data generated on the fly (two pass may be impossible)
* Memory-limited / data lives on hard disk, RAM much smaller, stream data into RAM to form sketch (two pass is just twice as expensive)
* Distributed / data lives on many different machines, expensive to communicate, hence better just to communicate sketches and add them up to form global sketch (one and two pass are possible)

Our one-pass algorithm can handle any of these; the two pass can handle the second two.
Our sketch just required a linear view of the data, so we don't require
fine-grained control over how the matrix entries are revealed.

# Distinctions compared to Becker's Tucker-TensorSketch

* Ours is a direct method, rather than sketch-and-solve
* Our method is computationally cheaper (faster)
* We find empirically that our method has lower error for the same memory
* Becker's paper does not present any theoretical results for the correctness;
it's relatively straightforward to use existing theory for the TensorSketch
to derive results about the multipass Tucker-TensorSketch
that bounds its error in the Frobenius norm.
However, it's not clear how to understand the performance of the single pass
Tucker-TensorSketch theoretically; and oddly, the multipass version
actually performs worse experimentally.
In contrast, our method allows us to control error both in the
Frobenius and operator norm for both the one and two pass algorithms.
This tighter control may explain why our method performs better empirically.
Also, as expected, the two pass algorithm does indeed outperform our
one pass algorithm, and for many matrices achieves compression ratios
comparable to the (many many pass) HOOI.
* Both methods are compatible with a variety of sketches.
These sketches give different tradeoffs between memory use and compression error.
We demonstrate this compatibility extensively in experiments.
(Whereas Becker's paper only uses TensorSketch w/CountSketch.)

SISC
SIMAX
SIMODS

# Nomenclature

factors U -> A
factor sketches G -> B
core sketch Z -> H
two pass -> two-pass
fix rank -> fixed rank

# New theory

Operator norm!

# Numerics

Log rel error of the 0 estimate is 0. Any algo with log rel error > 1 has some explaining to do.

Don't compare default settings. Only compare for same memory.
