# Importation des bibliothèques Autogen Studio nécessaires
import autogen
from autogen_studio import Presentation, Slide, Text, Image, HTML, CSS, youtube, gui

# Fonction pour créer une présentation simple
def create_presentation():
    # Créer une instance de la classe Presentation
    presentation = Presentation()

    # Créer une première diapositive avec du texte
    slide1 = Slide()
    title1 = Text("Introduction à Autogen Studio", font_size=40, bold=True)
    content1 = Text("Une introduction aux fonctionnalités de conception automatique de Autogen Studio.", font_size=20)
    slide1.add_element(title1)
    slide1.add_element(content1)
    presentation.add_slide(slide1)

    # Créer une deuxième diapositive avec une image
    slide2 = Slide()
    title2 = Text("Exemple de Projet", font_size=40, bold=True)
    image_path = "example_image.png"  # Remplacez par le chemin de votre image
    image2 = Image(image_path, width=500, height=300)
    slide2.add_element(title2)
    slide2.add_element(image2)
    presentation.add_slide(slide2)

    # Enregistrer la présentation créée
    presentation.save("ma_presentation.pptx")

# Fonction pour générer une page web simple
def generate_web_page(title, content):
    # Créer une instance de la classe HTML
    web_page = HTML()

    # Ajouter le titre à la page
    web_page.add_element("<head><title>" + title + "</title></head>")

    # Ajouter le contenu à la page
    web_page.add_element("<body>" + content + "</body>")

    # Enregistrer la page web générée
    web_page.save("index.html")

# Fonction principale
def main():
    print("Bienvenue dans le script d'Autogen Studio!")

    # Exemple de création de présentation
    create_presentation()

    print("La présentation a été créée avec succès. Consultez le fichier ma_presentation.pptx.")

    # Exemple de génération d'une page web
    title = "Ma Page Web"
    content = "<h1>Bienvenue sur ma page web générée par Autogen Studio!</h1>"
    generate_web_page(title, content)

    print("La page web a été générée avec succès. Consultez le fichier index.html.")

    # Définir les variables pour la vidéo YouTube
    fichier_video = "video.mp4"
    titre_video = "Ma vidéo"
    description_video = "Ceci est ma vidéo"
    tags_video = ["tag1", "tag2", "tag3"]

    # Créer une instance de la classe `youtube`
    youtube_instance = youtube()

    # Publier la vidéo sur YouTube
    youtube_instance.publier_video(fichier_video, titre_video, description_video, tags_video)

    # Définir les variables pour la page web avec données CSV
    fichier_donnees = "data.csv"
    nom_page = "index.html"

    # Créer une instance de la classe `page_web`
    page_web_instance = autogen.page_web(fichier_donnees)

    # Générer la page HTML et CSS
    page_web_instance.generer(nom_page)

    # Afficher la page web dans un navigateur
    gui.afficher_page_web(nom_page)

# Exécuter le script
if __name__ == "__main__":
    main()
