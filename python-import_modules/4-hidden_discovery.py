import importlib.util
import sys

def main():
    # Chemin vers le fichier hidden_4.pyc compilé
    module_path = '/tmp/hidden_4.pyc'
    
    # Charger le module compilé
    spec = importlib.util.spec_from_file_location("hidden_4", module_path)
    hidden_4 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_4)
    
    # Lister tous les noms dans le module hidden_4
    names = dir(hidden_4)
    
    # Filtrer et trier les noms qui ne commencent pas par __
    filtered_names = sorted(name for name in names if not name.startswith("__"))
    
    # Afficher chaque nom sur une nouvelle ligne
    for name in filtered_names:
        print(name)

# Exécuter le code uniquement si le script est exécuté directement
if __name__ == "__main__":
    main()
