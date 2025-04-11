import json
import streamlit as st
from src.threat_enrichment import ThreatEnrichment

class IncidentHandler:
    def __init__(self):
        self.enrichment = ThreatEnrichment()
        self.incident_data = {}

    def menu(self):
        print("\nSeleccione el tipo de incidente:")
        print("1. Phishing")
        print("2. Malware")
        print("3. Ransomware")
        choice = input("Ingrese su elección: ")

        if choice == "1":
            self.handle_phishing()
        elif choice == "2":
            self.handle_malware()
        elif choice == "3":
            self.handle_ransomware()
        else:
            print("Opción inválida.")

    def handle_phishing(self):
        print("\n--- Playbook de Phishing ---")

        email = input("Ingrese el correo sospechoso: ")
        link = input("Ingrese el enlace sospechoso: ")

        # Guardamos los datos iniciales
        self.incident_data = {
            "tipo": "Phishing",
            "email_sospechoso": email,
            "link_sospechoso": link,
            "acciones": [],
        }

        # Enriquecimiento
        self.enrichment.enrich_ioc(email)
        self.enrichment.enrich_ioc(link)

        # Contención
        self.incident_data["acciones"].append("Bloquear el dominio del enlace en el firewall.")
        self.incident_data["acciones"].append("Alertar a los usuarios sobre el intento de phishing.")

        print("Playbook de phishing completado con éxito.")
        
        # Guardar el reporte en JSON y permitir la descarga
        self.save_report()

    def handle_malware(self):
        print("\n--- Playbook de Malware ---")

        file_hash = input("Ingrese el hash del archivo sospechoso: ")
        filename = input("Ingrese el nombre del archivo sospechoso: ")

        # Guardamos los datos iniciales
        self.incident_data = {
            "tipo": "Malware",
            "hash_sospechoso": file_hash,
            "archivo_sospechoso": filename,
            "acciones": [],
        }

        # Enriquecimiento
        self.enrichment.enrich_ioc(file_hash)

        # Contención
        self.incident_data["acciones"].append("Aislar el equipo afectado de la red.")
        self.incident_data["acciones"].append("Analizar el archivo sospechoso en un entorno seguro.")
        self.incident_data["acciones"].append("Actualizar las firmas del antivirus y realizar un escaneo completo.")

        print("Playbook de malware completado con éxito.")
        
        # Guardar el reporte en JSON y permitir la descarga
        self.save_report()

    def handle_ransomware(self):
        print("\n--- Playbook de Ransomware ---")

        infected_system = input("Ingrese el nombre o IP del sistema comprometido: ")
        ransom_note = input("¿Se detectó nota de rescate? (Sí/No): ")

        # Guardamos los datos iniciales
        self.incident_data = {
            "tipo": "Ransomware",
            "sistema_infectado": infected_system,
            "nota_rescate_detectada": ransom_note,
            "acciones": [],
        }

        # Enriquecimiento
        self.enrichment.enrich_ioc(infected_system)

        # Contención
        self.incident_data["acciones"].append("Aislar el sistema comprometido inmediatamente.")
        self.incident_data["acciones"].append("Revisar respaldos recientes para recuperación.")
        self.incident_data["acciones"].append("Notificar al equipo legal y de cumplimiento, si corresponde.")
        self.incident_data["acciones"].append("Analizar la muestra del ransomware si está disponible.")

        print("Playbook de ransomware completado con éxito.")
        
        # Guardar el reporte en JSON y permitir la descarga
        self.save_report()

    def save_report(self):
        # Convertimos los datos a JSON
        report_json = json.dumps(self.incident_data, indent=2)

        # Usamos Streamlit para permitir la descarga del reporte
        filename = st.text_input("Ingrese el nombre para el archivo JSON:", "reporte_incidente.json")
        st.download_button(
            label="📥 Descargar Reporte en JSON",
            data=report_json,
            file_name=filename,
            mime="application/json"
        )

