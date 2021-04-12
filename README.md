# Micro template (for precomputed results)

### How to submit your system results to the STELLA infrastructure in 10 steps

This repository provides interested experimenters with a template for integrating their ranking and recommendation systems into the [STELLA infrastructure](https://stella-project.org/). In comparison to full-fledged systems (based on the [stella-micro-template](https://github.com/stella-project/stella-micro-template)), it may be more convenient for some participants to submit the system's output only. In this case, participants upload their runs with TREC file syntax [ here](https://lilas.stella-project.org/) and the results are integrated into the [STELLA app](https://github.com/stella-project/stella-app) for experimentation. More specifically, the workflow is as follows:

1. Decide if you want to contribute a document ranker (for the life sciences at [LIVIVO](https://www.livivo.de/)) or a dataset recommender (for the social sciences at [GESIS](https://www.gesis.org/en/home))
2. Depending on your chosen task, you have to download the corresponding datasets [here](https://th-koeln.sciebo.de/s/OBm0NLEwz1RYl9N)
3. Besides the datasets, you are provided with head queries (top-k queries) or head items (top-k target items of the recommendations)
4. Your systems have to index the datasets and rankings/recommendations should be retrieved with the help of the head queries/items
5. The results are supposed to be submitted with TREC run file syntax (see below). Each line contains the query/item identifier (`<qid>`), a string identifying the document (`<docid>`), an increasing rank number (`<rank>`), the corresponding score (`<score>`), and the tag chosen by the experimenters (`<identifier>`)

```
<qid> <Q0> <docid> <rank> <score> <identifier>
```

6. Save your run as a conventional `txt` file, e.g. as `ranking.txt`, and compress it as a `zip`, `tar.xz`, or `tar.gz` archive. Your compressed archive (containing a single `txt` file) is supposed to be uploaded.
7. Once you finish your developments, [register here](https://lilas.stella-project.org/) with an e-mail address, username, and a password.
8. Under the system settings you will be provided with a list of submitted systems. In order to upload your compressed archive, click on the `Upload Run File` button. Provide a system name, choose the task, select the local file of the compressed archive, and hit the `Submit` button.
9. After submission, a private GitHub-repository (containing your submission) will be set up in our organization. After the submitted results have been validated, the repository will be made public and is ready to be integrated into the [STELLA app](https://github.com/stella-project/stella-app). Revisit the systems overview in order to check if your system's status has been set from `submitted` to `running`. If it is `runnning`, the system is included in the next evaluation phase.
10. Once feedback data is available, you can revisit the Dashboard to download click feedbacks and gain first insights how your systems performs.
