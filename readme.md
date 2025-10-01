# file builder

[//]: # (todo : description)

# pip explication

installer toute les dernières version
```cmd
pip install -r requirements.txt
```

exemple ajouter une nouvelle lib
```cmd
pip install requests
pip freeze > requirements.txt
```

exemple mettre a jour les libs

```cmd
pip install --upgrade -r requirements.txt
pip freeze > requirements.txt
```