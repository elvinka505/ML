### 1. Загрузка + просмотр
```python
dataset = pd.read_csv("titanic.csv")
print(dataset.head())      # Первые 5 строк
print(dataset.tail())      # Последние 5
print(dataset.shape)       # (891, 12)
print(dataset.describe())  # Статистика
print(dataset.columns)     # ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', ...]
```

### 2. Фильтрация (без цепной индексации!)
```python
# Правильно
filtered = dataset[(dataset["Age"] > 20) & (dataset["Embarked"] == "S")]

# НЕ ДЕЛАТЬ (UserWarning)
dataset[dataset["Age"]>20]["Embarked"] == "S"

# .query()
dataset.query("Age > 20 and Embarked == 'S'")
```

### 3. Groupby + статистика
```python
dataset.groupby("Survived").size()  # 0: 549, 1: 342
pd.crosstab(dataset["Survived"], dataset["Sex"])  # выжившие по полу
dataset["Survived"].mean()  # 0.38 (38% выжили)
```

### 4. Графики (subplots)
```python
# 4 столбца рядом
fig, axes = plt.subplots(1, 4)
dataset.groupby("Survived").size().plot(kind="bar", ax=axes[0])
dataset.groupby("Sex").size().plot(kind="bar", ax=axes [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/images/74633895/5ad85a35-b163-435e-b902-8da56debecd1/Snimok-ekrana-2026-02-10-v-16.06.42.jpg?AWSAccessKeyId=ASIA2F3EMEYEQDNZSTYS&Signature=%2FQnChtPqDFcs4s%2FUdOhEL1PxHrM%3D&x-amz-security-token=IQoJb3JpZ2luX2VjECoaCXVzLWVhc3QtMSJHMEUCIGDSijs7KJHYSr%2Fi4DuolocjWEBcGz3h93wuhlrZt738AiEAjbfp4Rh1CYyFstVCrUDdCcFbx%2FngK7NQesTAg6jyaTgq%2FAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgw2OTk3NTMzMDk3MDUiDEviMwWz5kwlYKozACrQBL4KW6RqSJYCUU0z2w3VV8F7gpQIwABhDTn8DA7LutGME62mli2bIVGxRlvk%2FqrbHFE%2BQLutiAn6HqihZIwvJNN%2Bvtkkb6yz99NEXBLWl0HOfkie%2BAmB2rytWvFGrB8TuA63pCzyP5HQLE5bfch%2BGQ5o6KZVfJdINGlu45vgL2ikF7wMk4zfBEUcsIl85s1JUCfQZaoislT58ldeZZGL%2Bd94wYzMFaBp3VzeULk9mlMXLfSa5TFtScI%2FGmJcddz8Zj31xe%2BumPW7uzb5E3mtk3FrZYuvD%2BRBUWK%2FRKrCKYXlJ7Xe7BBgmzE2PPipr4SYo91DGj3v8O3szx%2FuQDlcUirEDOSNl2pSMEK%2FrqLAKYhKmjEkIiYGpknTaQERZCeYFHEOH7nVefg%2Fzc3WSijti%2BZPmWIuYHhzuAPfTHxXBE3etYJhV49JwnS3y40kDwN%2FZ6q%2BDUOko3t1ycMJ%2B80KsFBiHXGPOKhwn6ASgat9gXM7uXGVOlCPwnhFHYnvxzEbxYsfySMzIscLDrM%2FGW4fg2YahiamSVCys1WPoWFh2HN5HpOgwC1fEfQT%2F%2FhPVX%2FBai8H7LhH0%2FlvjkRKwv1BuFr900aaeQQ5qdFTglC8eicWQKBa5%2BLXc24WtNrYq7ZCPG8ZBO%2F0SFiy1nv3S7bY%2Bol1WPqSZUumxaz%2B5Ux1zkR5p9IdrT89yIr4phAoPnBzLA8b7NCQrTcX5CjVPhwW2klqRf0W6IEj9px%2FvKX8y434Ldv60QU2u%2FABNEXSKV%2B%2BFnEJ%2Bg5PFpWIjweYZu1XN9Mwu8u9zAY6mAHly6G8mnq%2FOKzOZjeilk6pyDarwlodeNrtL40zoG6RdPzYPKgFVBX4EVA%2Fa6yIiTbVOs9fLVuPG1hnPAtcFfEd1imlKNviL3nwfZA5MCgxTBy1sukLsetkfTMGvgI22PdWil%2FZYkrqF0inTiezqiykYydm7bJidcv%2BeTfDiWyHlzP7u6lUiz0tIhPKV9v6EtLe%2FfpTG9TMrg%3D%3D&Expires=1771008171))
# ...
plt.show()

# 2 столбца
fig, axes = plt.subplots(1, 2)
# ...
```
