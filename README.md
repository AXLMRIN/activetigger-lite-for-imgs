# activetigger-lite-for-imgs

Set up conda environment:

```bash
conda create -n activetigger-lite-for-images python=3.12 -y
conda activate activetigger-lite-for-images
conda install pandas numpy streamlit -y
```

Write your labels in the `labels.txt`, one line = one label (except empty lines). Put your images in the `img` folder, the name of the file is the index. Launch the app and annotate. Once finished, your annotations are stored in the `annotations.csv` file.

Launch app :

```bash
streamlit run app.py
```
