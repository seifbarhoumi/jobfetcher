import os

from utils.csv_writer import save_csv
from utils.logger import logger


def process_and_store_data(offres, departement, type_contrat, export_csv):
    """Transforme et stocke les données des offres, entreprises, compétences, formations et autres détails."""

    if not offres:
        logger.warning("⚠️ Aucune offre à traiter.")
        return

    output_dir = f"outputs/{departement}/{type_contrat}"
    os.makedirs(output_dir, exist_ok=True)

    offres_data = [
        [
            o.get("id"),
            o.get("intitule", "N/A"),
            o.get("description", "N/A"),
            o.get("dateCreation", "N/A"),
            o.get("dateActualisation", "N/A"),
            o.get("lieuTravail", {}).get("libelle", "N/A"),
            o.get("lieuTravail", {}).get("codePostal", "N/A"),
            o.get("romeCode", "N/A"),
            o.get("romeLibelle", "N/A"),
            o.get("appellationlibelle", "N/A"),
            o.get("typeContratLibelle", "N/A"),
            o.get("experienceLibelle", "N/A"),
            o.get("salaire", {}).get("libelle", "N/A"),
            o.get("dureeTravailLibelleConverti", "N/A"),
            o.get("conditionExercice", "N/A"),
            o.get("alternance", "N/A"),
            o.get("nombrePostes", "N/A"),
            o.get("secteurActiviteLibelle", "N/A"),
            o.get("qualificationLibelle", "N/A"),
            o.get("trancheEffectifEtab", "N/A"),
            o.get("offresManqueCandidats", "N/A")
        ]
        for o in offres
    ]

    entreprises_data = [
        [
            o.get("id"),
            o.get("entreprise", {}).get("nom", "N/A"),
            o.get("entreprise", {}).get("description", "N/A"),
            o.get("entreprise", {}).get("logo", "N/A"),
            o.get("entreprise", {}).get("url", "N/A"),
            o.get("entreprise", {}).get("entrepriseAdaptee", "N/A")
        ]
        for o in offres if "entreprise" in o
    ]

    competences_data = [
        [
            o.get("id"),
            c.get("code", "N/A"),
            c.get("libelle", "N/A"),
            c.get("exigence", "N/A")
        ]
        for o in offres for c in o.get("competences", [])
    ]

    logger.info("📊 Transformation des données terminée.")

    if export_csv:
        save_csv(f"{output_dir}/offres_d_emploi.csv", offres_data, [
            "ID", "Intitulé", "Description", "Date_Création", "Date_Actualisation",
            "Lieu", "Code_Postal", "Code_ROME", "Libellé_ROME", "Appellation",
            "Type_Contrat", "Expérience", "Salaire", "Durée_Travail",
            "Conditions_Exercice", "Alternance", "Nombre_Postes", "Secteur_Activité",
            "Qualification", "Effectif_Établissement", "Manque_Candidats"
        ])

        save_csv(f"{output_dir}/entreprises.csv", entreprises_data, [
            "Offre_ID", "Nom", "Description", "Logo", "URL", "Entreprise_Adaptee"
        ])

        save_csv(f"{output_dir}/competences.csv", competences_data, [
            "Offre_ID", "Code_Compétence", "Libellé_Compétence", "Exigence"
        ])

        logger.info(f"✅ Export CSV terminé pour {departement}/{type_contrat} !")
