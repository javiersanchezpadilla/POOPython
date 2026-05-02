""" PATRON FACTORY (CREACIONAL)

    Fábrica de Formatos de Reporte (Exportación)
    --------------------------------------------
    Un sistema que genera reportes en diferentes extensiones.
"""
class ReportePDF:
    def generar(self): return "Generando archivo .pdf 📄"

class ReporteExcel:
    def generar(self): return "Generando archivo .xlsx 📊"

class FabricaReportes:
    @staticmethod
    def crear_reporte(formato):
        if formato == "pdf": return ReportePDF()
        if formato == "excel": return ReporteExcel()

# Uso: El usuario elige el formato en la interfaz.
mi_reporte = FabricaReportes.crear_reporte("excel")
print(mi_reporte.generar())
