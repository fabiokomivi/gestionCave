from setuptools import setup

setup(
    name='MonApplicationTkinter',  # Nom de ton application
    version='0.1',  # Version de ton application
    description='Une application simple avec Tkinter',  # Description de ton application
    author='Ton Nom',  # Ton nom ou celui de l'auteur
    author_email='tonemail@example.com',  # Ton adresse email
    packages=['.'],  # Inclut le package actuel (qui contient main.py)
    entry_points={
        'gui_scripts': [
            'monapplication=main:main',  # Remplace main par le nom de la fonction principale si elle est différente
        ],
    },
    install_requires=[
        # Liste des dépendances requises par ton application (vide pour Tkinter)
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Version minimum de Python requise
)
