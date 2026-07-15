# -*- coding: utf-8 -*-
"""Propuesta visual Observatorio CTi: compacta, flujo full-width, KPIs + MVP."""
from pathlib import Path
import json

OUT = Path(__file__).resolve().parent

def fmt_cop(n):
    return f"${n:,.0f}".replace(",", ".")

# Flujo compacto (cabe completo en viewport)
FLOW = [
    {"id": "demanda", "n": 1, "titulo": "Demanda", "fase": "Entrada", "x": 20, "y": 150, "w": 100, "h": 56, "tipo": "entrada",
     "proceso": "Priorizar necesidades de información del CMA.",
     "actividades": ["Recibir solicitudes", "Priorizar estudios", "Alinear con CEITTO"],
     "entradas": "Solicitudes institucionales", "salidas": "Alcance priorizado",
     "responsable": "Analista de datos · área solicitante"},
    {"id": "fuentes", "n": 2, "titulo": "Fuentes", "fase": "Captura", "x": 150, "y": 50, "w": 100, "h": 56, "tipo": "dato",
     "proceso": "Buscar en fuentes secundarias nacionales e internacionales.",
     "actividades": ["Seleccionar bases VT/IC", "Consultar repositorios", "Registrar evidencias"],
     "entradas": "Alcance y palabras clave", "salidas": "Conocimiento explícito",
     "responsable": "Analista de datos"},
    {"id": "tacito", "n": 3, "titulo": "Tácito", "fase": "Captura", "x":.150, "y": 250, "w": 100, "h": 56, "tipo": "dato",
     "proceso": "Capturar conocimiento de actores clave.",
     "actividades": ["Entrevistas", "Eventos y foros", "Registrar necesidades"],
     "entradas": "Actores y eventos", "salidas": "Conocimiento tácito",
     "responsable": "Analista de datos"},
    {"id": "captura", "n": 4, "titulo": "Captura", "fase": "Proceso", "x": 280, "y": 150, "w": 100, "h": 56, "tipo": "proceso",
     "proceso": "Integrar información con instrumentos de captura.",
     "actividades": ["Aplicar instrumentos", "Homogeneizar formatos", "Clasificar por tema"],
     "entradas": "Explícito + tácito", "salidas": "Base estructurada",
     "responsable": "Analista de datos"},
    {"id": "tratamiento", "n": 5, "titulo": "Tratamiento", "fase": "Proceso", "x": 410, "y": 150, "w": 100, "h": 56, "tipo": "proceso",
     "proceso": "Organizar, cuantificar y procesar la información.",
     "actividades": ["Validar datos", "Consolidar indicadores", "Preparar insumos"],
     "entradas": "Base estructurada", "salidas": "Dataset tratado",
     "responsable": "Analista de datos"},
    {"id": "vtic", "n": 6, "titulo": "VT / IC", "fase": "Análisis", "x": 540, "y": 50, "w": 100, "h": 56, "tipo": "proceso",
     "proceso": "Ejecutar vigilancia tecnológica e inteligencia competitiva.",
     "actividades": ["Estudios VT/IC", "Patentabilidad", "Análisis de entorno"],
     "entradas": "Dataset tratado", "salidas": "Informes VT/IC",
     "responsable": "Analista de datos · CEITTO"},
    {"id": "tendencias", "n": 7, "titulo": "Tendencias", "fase": "Análisis", "x": 540, "y": 250, "w": 100, "h": 56, "tipo": "proceso",
     "proceso": "Identificar tendencias y oportunidades en CTi.",
     "actividades": ["Monitorear señales", "Detectar oportunidades", "Leer necesidades"],
     "entradas": "Dataset tratado", "salidas": "Mapa de tendencias",
     "responsable": "Analista de datos"},
    {"id": "productos", "n": 8, "titulo": "Productos", "fase": "Salida", "x": 670, "y": 150, "w": 100, "h": 56, "tipo": "salida",
     "proceso": "Empaquetar información de alto valor.",
     "actividades": ["Boletines", "Reportes", "Asesorías"],
     "entradas": "Resultados de análisis", "salidas": "Productos accionables",
     "responsable": "Analista de datos · CEITTO"},
    {"id": "difusion", "n": 9, "titulo": "Difusión", "fase": "Salida", "x": 800, "y": 150, "w": 100, "h": 56, "tipo": "salida",
     "proceso": "Divulgar oportunidades y fortalecer capacidades CTIC.",
     "actividades": ["Canales institucionales", "Charlas y encuentros", "Actores estratégicos"],
     "entradas": "Productos", "salidas": "Comunidad informada",
     "responsable": "Observatorio · comunicaciones"},
    {"id": "decision", "n": 10, "titulo": "Decisión", "fase": "Cierre", "x": 930, "y": 150, "w": 100, "h": 56, "tipo": "salida",
     "proceso": "Apoyar decisiones con evidencia y cerrar el ciclo.",
     "actividades": ["Entrega a dirección", "Retroalimentar ciclo", "Ajustar prioridades"],
     "entradas": "Productos difundidos", "salidas": "Decisiones · nueva demanda",
     "responsable": "Dependencias usuarias"},
]

# fix typo x =.150
FLOW[2]["x"] = 150

FLOW_EDGES = [
    ("demanda", "fuentes"), ("demanda", "tacito"),
    ("fuentes", "captura"), ("tacito", "captura"),
    ("captura", "tratamiento"),
    ("tratamiento", "vtic"), ("tratamiento", "tendencias"),
    ("vtic", "productos"), ("tendencias", "productos"),
    ("productos", "difusion"), ("difusion", "decision"),
    ("decision", "demanda"),
]

OBJ = [
    {"n": "01", "t": "Identificar tendencias CTi", "s": "Monitoreo permanente",
     "d": "Detectar tendencias en Ciencia, Tecnología e Innovación relevantes para el CMA."},
    {"n": "02", "t": "Definir captura de datos", "s": "Instrumentos y calidad",
     "d": "Definir instrumentos para capturar y procesar información confiable y trazable."},
    {"n": "03", "t": "Observar el entorno", "s": "Industria, academia e investigación",
     "d": "Leer necesidades de industria, academia e investigación para aportar al desarrollo empresarial."},
    {"n": "04", "t": "Apoyar decisiones", "s": "Información de alto valor",
     "d": "Entregar alertas, boletines y estudios VT/IC a las dependencias del CMA."},
]

PILARES = [
    {"t": "Alerta", "d": "Recopilar información del entorno para adaptarse a tiempo."},
    {"t": "Tendencias", "d": "Entregar señales útiles a las áreas de CTi."},
    {"t": "Oportunidad", "d": "Detectar financiamiento, negocios y temas prioritarios."},
]

VENTAJAS = [
    {"t": "Financiamiento", "d": "Oportunidades para proyectos y nuevos negocios"},
    {"t": "Anticipación", "d": "Adelantarse a cambios del entorno"},
    {"t": "Alertas", "d": "Monitoreo permanente por temática"},
    {"t": "Mercado", "d": "Necesidades de industria"},
    {"t": "Tendencias", "d": "Sectores de interés"},
    {"t": "Estrategia", "d": "Decisiones con evidencia"},
    {"t": "Innovación", "d": "Acelerar la innovación"},
]

PLAN = [
    {"fase": "01", "t": "Diseño", "items": [
        "Procedimiento, objetivos y flujo",
        "Instrumento de oportunidades CTi",
        "Plan de acción 2026-2027",
        "Mecanismos de captura y divulgación",
        "Primer boletín piloto",
    ]},
    {"fase": "02", "t": "Necesidades", "items": [
        "Facultades e Investigación/Extensión",
        "CEITTO: innovación, PI, emprendimiento",
        "Direcciones y Bienestar",
        "Boletines piloto 1 y 2",
        "Instrumentos de demanda industria",
    ]},
    {"fase": "03", "t": "Modelo", "items": [
        "Marco conceptual del Observatorio",
        "Diagnóstico estructural",
        "Organización y sostenibilidad",
        "Sistemas y fuentes de información",
        "Informes, difusión y conocimiento",
    ]},
]

SERVICIOS = [
    {"t": "Tendencias", "d": "Áreas de oportunidad en CTi"},
    {"t": "Monitoreo", "d": "Necesidades de industria y academia"},
    {"t": "VT / IC", "d": "Estudios a la medida"},
    {"t": "Prospectiva", "d": "Escenarios futuros"},
    {"t": "Patentabilidad", "d": "Estado de la técnica"},
    {"t": "Capacitación", "d": "Asesoría en VT/IC"},
    {"t": "Estado del arte", "d": "Apoyo a investigación"},
    {"t": "Transferencia", "d": "Modelos de negocio"},
]

CANALES = [
    "Convocatorias", "Eventos", "Mural", "Cátedra", "Buzón", "Afiches",
    "Charlas", "Reuniones", "Actores", "Publicaciones", "Jornadas", "Medios",
]

ESTUDIOS = [
    {
        "id": "camara",
        "t": "Cámara de Comercio",
        "d": "Análisis RNT en 5 subregiones de Antioquia",
        "metric": "5",
        "metric_l": "subregiones",
        "tag": "Territorio · RNT",
        "blurb": "Informe interactivo de análisis del Registro Nacional de Turismo por subregiones, con lectura territorial para decisión empresarial e institucional.",
        "evidencias": [
            {"tipo": "html", "label": "Análisis RNT subregiones", "src": "evidencias/camara/analisis-rnt-subregiones.html"},
        ],
    },
    {
        "id": "magdalena",
        "t": "Magdalena medio",
        "d": "Paisaje ganadero y desarrollo territorial",
        "metric": "8+",
        "metric_l": "entregables locales",
        "tag": "Territorio · agro",
        "blurb": "Estudios del paisaje ganadero del Magdalena Medio: atractivos, ruta Puerto Berrío-Maceo, benchmarking, modelo de negocio y taller PCG. La plataforma web se abre en pestaña nueva.",
        "evidencias": [
            {"tipo": "html", "label": "Atractivos turísticos", "src": "evidencias/magdalena/atractivos-turisticos.html"},
            {"tipo": "html", "label": "Dashboard taller PCG", "src": "evidencias/magdalena/dashboard-taller-pcg.html"},
            {"tipo": "html", "label": "Informe taller PCG", "src": "evidencias/magdalena/informe-taller-pcg.html"},
            {"tipo": "html", "label": "Ruta Puerto Berrío-Maceo", "src": "evidencias/magdalena/ruta-puerto-berrio-maceo.html"},
            {"tipo": "html", "label": "Análisis RNT Puerto Berrío", "src": "evidencias/magdalena/analisis-rnt-puerto-berrio.html"},
            {"tipo": "html", "label": "Rutas proyectadas", "src": "evidencias/magdalena/rutas-proyectadas.html"},
            {"tipo": "html", "label": "Modelo de negocio", "src": "evidencias/magdalena/modelo-negocio.html"},
            {"tipo": "html", "label": "Benchmarking PCC", "src": "evidencias/magdalena/benchmarking-pcc.html"},
            {"tipo": "html", "label": "Mapa georreferenciación", "src": "evidencias/magdalena/mapa-georreferenciacion.html"},
            {"tipo": "url", "label": "Plataforma web (Vercel)", "src": "https://mgdalena-medio.vercel.app/"},
        ],
    },
    {
        "id": "do",
        "t": "Denominación de origen",
        "d": "Tapetusa artesanal y reconocimiento DOP",
        "metric": "12+",
        "metric_l": "anexos y tableros",
        "tag": "DOP · CEITTO",
        "blurb": "Expediente técnico con percepción territorial, tableros Power BI, misión técnica, infografías y guías para autoridades y productores.",
        "evidencias": [
            {"tipo": "html", "label": "Infografía Tapetusa", "src": "evidencias/do/infografia-tapetusa-profesional.html"},
            {"tipo": "html", "label": "Infografía actualizada", "src": "evidencias/do/infografia-tapetusa-actualizada.html"},
            {"tipo": "pdf", "label": "Tableros Power BI", "src": "evidencias/do/anexo-4-screenshot-tableros-power-bi.pdf"},
            {"tipo": "pdf", "label": "Gráfico de resultados", "src": "evidencias/do/anexo-1-gr-fico-de-resultados.pdf"},
            {"tipo": "pdf", "label": "Tabla de resultados", "src": "evidencias/do/anexo-1-tabla-de-resultados.pdf"},
            {"tipo": "pdf", "label": "Percepción municipios", "src": "evidencias/do/anexo-3-an-lisis-de-percepci-n-de-los-municipios.pdf"},
            {"tipo": "pdf", "label": "Matriz diagnóstico", "src": "evidencias/do/anexo-5-matriz-diagnostico-de-los-municipios.pdf"},
            {"tipo": "pdf", "label": "Informe misión técnica DOP", "src": "evidencias/do/anexo-8-informe-final-misi-n-t-cnica-dop.pdf"},
            {"tipo": "pdf", "label": "Evidencia del viaje", "src": "evidencias/do/anexo-9-evidencia-del-viaje.pdf"},
            {"tipo": "pdf", "label": "BPM Tapetusa", "src": "evidencias/do/bpm-tapetusa.pdf"},
        ],
    },
    {
        "id": "penol",
        "t": "Peñol",
        "d": "RNT territorial y potencial turístico",
        "metric": "2",
        "metric_l": "informes HTML",
        "tag": "Turismo · RNT",
        "blurb": "Webscraping del RNT y reporte turístico del municipio de Peñol como apoyo a la lectura competitiva del destino.",
        "evidencias": [
            {"tipo": "html", "label": "Informe webscraping Peñol", "src": "evidencias/penol/informe-webscraping-penol.html"},
            {"tipo": "html", "label": "Informe turístico Peñol", "src": "evidencias/penol/informe-turistico-penol.html"},
        ],
    },
    {
        "id": "comfama",
        "t": "Comfama",
        "d": "Madurez de la Ruta Lechera San Pedro",
        "metric": "1",
        "metric_l": "informe de madurez",
        "tag": "Rutas · turismo",
        "blurb": "Diagnóstico de madurez de la ruta lechera / San Pedro como insumo de vigilancia e inteligencia para el entorno turístico.",
        "evidencias": [
            {"tipo": "html", "label": "Informe madurez Ruta San Pedro", "src": "evidencias/comfama/informe-madurez-ruta-san-pedro.html"},
        ],
    },
    {
        "id": "convocatorias",
        "t": "Convocatorias",
        "d": "Radar de oportunidades de financiación",
        "metric": "30+",
        "metric_l": "oportunidades/mes (meta)",
        "tag": "Radar · I+D+i",
        "blurb": "ConvoRadar opera como dashboard en vivo. Por seguridad del navegador no se embebe: ábrelo en una pestaña nueva para ver el tablero completo.",
        "evidencias": [
            {"tipo": "url", "label": "ConvoRadar dashboard", "src": "https://convocaradar-web.vercel.app/dashboard"},
            {"tipo": "url", "label": "ConvoRadar inicio", "src": "https://convocaradar-web.vercel.app/"},
        ],
    },
    {
        "id": "investigacion",
        "t": "Investigación",
        "d": "Proyectos finalizados con evidencia entregable",
        "metric": "N",
        "metric_l": "cierres documentados",
        "tag": "Proyectos",
        "blurb": "Capacidad demostrada para cerrar estudios VT/IC con productos accionables para dependencias y aliados.",
        "evidencias": [],
    },
]

LINEAS = [
    {"t": "Gestión empresarial", "d": "Productividad y competitividad"},
    {"t": "VT / IC", "d": "Vigilancia e inteligencia"},
    {"t": "Patentabilidad", "d": "Estado de la técnica"},
]

CAPACIDADES = [
    {"t": "Analista de datos", "d": "Un perfil con experiencia para operar el Observatorio."},
    {"t": "Software especializado", "d": "Acceso a herramientas de análisis y vigilancia."},
    {"t": "Red Innruta", "d": "Inteligencia competitiva y sus plataformas."},
    {"t": "Red Secopind", "d": "Propiedad intelectual · ICIPC."},
]

# Contextualizado a Colmayor (PDI 2024-2028, CNA, CEITTO, Alcaldía de Medellín)
PROBLEMAS = [
    {
        "id": "P1", "tipo": "alerta", "titulo": "Información dispersa",
        "colmayor": "Académico, administrativo y de entorno en sistemas separados",
        "desc": "En Colmayor, los datos de facultades, investigación, extensión, bienestar y planeación suelen vivir en formatos y sistemas distintos. Eso dificulta el seguimiento del Plan Indicativo y retrasa reportes para dirección, MIPG y autoevaluación.",
        "efecto": "Se pierde trazabilidad, se duplican esfuerzos y las decisiones llegan tarde.",
    },
    {
        "id": "P2", "tipo": "alerta", "titulo": "Convocatorias sin trazabilidad",
        "colmayor": "Oportunidades de I+D+i, extensión y CEITTO",
        "desc": "Sin mapeo continuo, grupos, semilleros y el CEITTO (emprendimiento, innovación, transferencia y propiedad intelectual) detectan tarde convocatorias locales, nacionales e internacionales.",
        "efecto": "Se reducen postulaciones oportunas y la articulación con el entorno productivo de Medellín y Antioquia.",
    },
    {
        "id": "P3", "tipo": "alerta", "titulo": "Entorno cambiante",
        "colmayor": "Políticas públicas, tecnología y territorio",
        "desc": "Como institución adscrita a la Alcaldía de Medellín, Colmayor necesita leer cambios educativos, tecnológicos y normativos que afectan programas, extensión, internacionalización y acompañamiento territorial (incluido Presupuesto Participativo).",
        "efecto": "Sin vigilancia estructurada (UNE 166006, ISO 56002, ISO 31000) la adaptación institucional llega con retraso.",
    },
    {
        "id": "P4", "tipo": "neutral", "titulo": "Brecha analítica",
        "colmayor": "Acreditación CNA y calidad académica",
        "desc": "El aseguramiento de la calidad y la renovación de acreditación exigen evidencia consolidada. La brecha analítica limita indicadores CNA, rankings y la investigación aplicada con el sector productivo.",
        "efecto": "Más carga manual en autoevaluación y menor capacidad de anticipar hallazgos de calidad.",
    },
    {
        "id": "P5", "tipo": "neutral", "titulo": "Gobernanza de datos",
        "colmayor": "Confianza institucional y ecosistema tecnológico",
        "desc": "Hace falta un marco formal de privacidad (Ley 1581), roles de datos y criterios éticos para usar información e inteligencia analítica con confianza, en línea con la Línea 3 del PDI (gestión integral de la información).",
        "efecto": "Sin gobierno claro, es difícil integrar fuentes y sostener una cultura de datos alineada al PETIC.",
    },
    {
        "id": "P6", "tipo": "solucion", "titulo": "Respuesta del Observatorio",
        "colmayor": "Capacidad permanente de inteligencia institucional",
        "desc": "El Observatorio CTi articula arquitectura de datos, gobierno de información, tableros ejecutivos y productos de vigilancia tecnológica e inteligencia competitiva para las dependencias del CMA.",
        "efecto": "Pasa de reportes fragmentados a evidencia útil para planeación, calidad, investigación y extensión.",
    },
]

# Ventajas no monetarias alineadas al Plan de Desarrollo 2024-2028
VENTAJAS_PDI = [
    {
        "linea": "L1",
        "nombre": "Academia transformadora de vidas",
        "foco": "Diversidad, equidad, calidad e inclusión",
        "indicadores": [
            {"t": "Evidencia para autoevaluación CNA", "m": "Expedientes de calidad con datos trazables por factor"},
            {"t": "Tiempo de reporte académico", "m": "Meta orientativa: reducir al menos 20% el tiempo de consolidación"},
            {"t": "Permanencia y graduación", "m": "Tableros de bienestar y éxito académico (piloto del Observatorio)"},
            {"t": "Apoyo a decanos y programas", "m": "Respuesta a solicitudes de información en máximo 5 días hábiles"},
        ],
    },
    {
        "linea": "L2",
        "nombre": "Intercambio de saberes",
        "foco": "Investigación, innovación, emprendimiento y proyección social",
        "indicadores": [
            {"t": "Convocatorias detectadas a tiempo", "m": "Meta orientativa: al menos 30 oportunidades mapeadas al mes"},
            {"t": "Productos VT/IC para el entorno", "m": "Al menos 2 reportes de inteligencia al mes"},
            {"t": "Articulación con sector productivo", "m": "Estudios y alertas útiles a extensión y CEITTO"},
            {"t": "Apoyo a grupos y semilleros", "m": "Estado del arte y vigilancia para proyectos y postulaciones"},
        ],
    },
    {
        "linea": "L3",
        "nombre": "Ecosistema tecnológico Colmayor",
        "foco": "Interoperabilidad, información y mejora continua",
        "indicadores": [
            {"t": "Fuentes institucionales integradas", "m": "Meta orientativa: al menos 5 fuentes al mes 6"},
            {"t": "Disponibilidad de tableros", "m": "Meta: disponibilidad igual o superior a 99,5%"},
            {"t": "Cultura de datos", "m": "Procedimientos, catálogo de fuentes y roles documentados (PETIC)"},
            {"t": "Continuidad operativa", "m": "Infraestructura TI con respaldo energético y garantía en sitio"},
        ],
    },
    {
        "linea": "L4",
        "nombre": "Sostenibilidad y gestión humana",
        "foco": "Planeación, capacidad instalada e identidad institucional",
        "indicadores": [
            {"t": "Soporte al Plan Indicativo", "m": "Datos oportunos para seguimiento de líneas y metas"},
            {"t": "Decisiones directivas con evidencia", "m": "Meta orientativa: al menos 3 decisiones documentadas por trimestre"},
            {"t": "Uso compartido de capacidad", "m": "Workstation disponible para Observatorio y otros procesos priorizados"},
            {"t": "Transparencia operativa", "m": "Trazabilidad de fuentes, productos y responsables"},
        ],
    },
]

KPIS = [
    {"id": "KPI-01", "dim": "operativa", "nombre": "Disponibilidad del servidor", "meta": "≥ 99% mensual"},
    {"id": "KPI-02", "dim": "operativa", "nombre": "Tiempo de integración de datos", "meta": "< 2 horas/día"},
    {"id": "KPI-03", "dim": "operativa", "nombre": "Disponibilidad de tableros", "meta": "≥ 99,5%"},
    {"id": "KPI-04", "dim": "operativa", "nombre": "Recuperación ante fallo energético", "meta": "0 pérdida de datos"},
    {"id": "KPI-05", "dim": "analitica", "nombre": "Convocatorias mapeadas/mes", "meta": "≥ 30"},
    {"id": "KPI-06", "dim": "analitica", "nombre": "Reportes de inteligencia/mes", "meta": "≥ 2"},
    {"id": "KPI-07", "dim": "analitica", "nombre": "Fuentes de datos integradas", "meta": "≥ 5 al mes 6"},
    {"id": "KPI-08", "dim": "analitica", "nombre": "Tiempo respuesta directivos", "meta": "≤ 5 días hábiles"},
    {"id": "KPI-09", "dim": "analitica", "nombre": "Precisión clasificación convocatorias", "meta": "≥ 85%"},
    {"id": "KPI-10", "dim": "roi", "nombre": "Valor convocatorias postuladas", "meta": "≥ COP 30M adjudicadas"},
    {"id": "KPI-11", "dim": "roi", "nombre": "Tasa conversión convocatorias", "meta": "≥ 30% postulación"},
    {"id": "KPI-12", "dim": "roi", "nombre": "Ahorro herramientas externalizadas", "meta": "≥ 70% reducción"},
    {"id": "KPI-13", "dim": "roi", "nombre": "Reducción horas recopilación manual", "meta": "≥ 40%"},
    {"id": "KPI-14", "dim": "roi", "nombre": "Ingresos servicios externos", "meta": "≥ COP 10M año 1"},
    {"id": "KPI-15", "dim": "roi", "nombre": "Propuestas comerciales enviadas", "meta": "≥ 2 al mes 6"},
    {"id": "KPI-16", "dim": "roi", "nombre": "Reducción tiempo acreditación", "meta": "≥ 20%"},
    {"id": "KPI-17", "dim": "roi", "nombre": "Decisiones con evidencia", "meta": "≥ 3/trimestre"},
    {"id": "KPI-18", "dim": "sostenibilidad", "nombre": "ROI acumulado hardware", "meta": "≥ 50% al mes 6"},
    {"id": "KPI-19", "dim": "sostenibilidad", "nombre": "Punto de equilibrio", "meta": "mes 6–14"},
    {"id": "KPI-20", "dim": "sostenibilidad", "nombre": "Índice autofinanciamiento", "meta": "≥ 30% al mes 6"},
]

DIM_LABEL = {
    "operativa": "Operativa",
    "analitica": "Analítica",
    "roi": "ROI",
    "sostenibilidad": "Sostenibilidad",
}

HW = {
    "ws": {
        "titulo": "Workstation IA · Ryzen 9 9950X + RTX 5090",
        "specs": [
            "AMD Ryzen 9 9950X (16 núcleos / 32 hilos)",
            "192 GB DDR5 · NVIDIA GeForce RTX 5090 32 GB",
            "SSD NVMe 2 TB · fuente ≥1.200 W · AIO 360",
            "Windows 11 Pro · ensamble y garantía ≥2 años",
            "Cotización distribuidores CO · carrito mixto (jul-2026)",
        ],
        "cop": 37_081_000,
    },
    "ups": {
        "titulo": "Eaton DX2000LAN",
        "specs": [
            "Online doble conversión",
            "2000 VA / 1800 W",
            "Autonomía 5–15 min según carga",
            "Cubre consumo estimado del workstation bajo carga",
        ],
        "cop": 2_400_000,
    },
}

_ws = HW["ws"]["cop"]
_ups = HW["ups"]["cop"]
_ia = 4_500_000 + 7_600_000  # antes: red/conectividad + implementación
_total = _ws + _ups + _ia
PRESUPUESTO = {
    "total": _total,
    "lineas": [
        {"nombre": "Workstation IA (Ryzen 9 9950X + RTX 5090)", "valor": _ws, "pct": round(_ws / _total * 100, 1)},
        {"nombre": "UPS Eaton DX2000LAN", "valor": _ups, "pct": round(_ups / _total * 100, 1)},
        {"nombre": "Implementación de IA", "valor": _ia, "pct": round(_ia / _total * 100, 1)},
    ],
}

FUENTES = ["Scopus", "ScienceDirect", "IEEE", "EBSCO", "Embase", "Reaxys", "Engineering Village", "e-libro"]


def node_cx(n):
    return n["x"] + n["w"] / 2


def node_cy(n):
    return n["y"] + n["h"] / 2


def edge_d(a, b, cyclic=False):
    ax, ay, bx, by = node_cx(a), node_cy(a), node_cx(b), node_cy(b)
    if cyclic:
        return f"M {ax} {ay + 28} C {ax} {ay + 120}, {bx} {by + 120}, {bx} {by + 28}"
    mx = (ax + bx) / 2
    return f"M {ax} {ay} C {mx} {ay}, {mx} {by}, {bx} {by}"


nmap = {n["id"]: n for n in FLOW}
edges_svg = []
for a, b in FLOW_EDGES:
    cyclic = a == "decision" and b == "demanda"
    edges_svg.append(
        f'<path class="{"flecha ciclo" if cyclic else "flecha"}" d="{edge_d(nmap[a], nmap[b], cyclic)}" marker-end="url(#{ "arrowC" if cyclic else "arrow" })"/>'
    )
if True:
    edges_svg.append('<text class="lbl-ciclo" x="480" y="345">Ciclo de mejora continua</text>')

nodes_svg = []
for n in FLOW:
    nodes_svg.append(f'''<g class="nodo" data-id="{n['id']}" transform="translate({n['x']},{n['y']})">
      <rect class="hit" width="{n['w']}" height="{n['h']}" fill="transparent"/>
      <rect class="caja caja-{n['tipo']}" width="{n['w']}" height="{n['h']}" rx="10"/>
      <circle class="badge" cx="13" cy="13" r="10"/>
      <text class="badge-n" x="13" y="17">{n['n']}</text>
      <text class="fase" x="{n['w']/2}" y="20">{n['fase']}</text>
      <text class="tit" x="{n['w']/2}" y="38">{n['titulo']}</text>
    </g>''')

f0 = FLOW[0]
OBJETIVO_CLARO = (
    "Identificar tendencias y oportunidades en Ciencia, Tecnología e Innovación "
    "para el CMA, transformando información del entorno en insumos para la decisión institucional."
)

kpi_cards = "".join(
    f'''<article class="kpi" data-dim="{k['dim']}">
      <div class="kpi-top"><span class="kid">{k['id']}</span><span class="kdim">{DIM_LABEL[k['dim']]}</span></div>
      <h4>{k['nombre']}</h4>
      <p>{k['meta']}</p>
    </article>'''
    for k in KPIS
)

html = f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Observatorio CTi | Propuesta | CEITTO Colmayor</title>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet"/>
<style>
:root {{
  --bg:#f6faff; --surface:#fff; --alt:#eef4fc; --ink:#151c22; --charcoal:#2C3339;
  --mute:#4E5A64; --orange:#F39A1A; --teal:#00B3AF; --teal-deep:#006a67; --primary:#875200;
  --line:rgba(44,51,57,.12); --shadow:0 10px 28px rgba(44,51,57,.08);
  --r:12px; --font:"Inter",system-ui,sans-serif; --display:"Hanken Grotesk",Georgia,serif;
}}
*{{box-sizing:border-box;margin:0;padding:0}}
html{{scroll-behavior:smooth;scroll-padding-top:72px}}
html{{scroll-behavior:smooth;scroll-padding-top:76px}}
body{{font-family:var(--font);background:var(--bg);color:var(--ink);font-size:17px;line-height:1.55;-webkit-font-smoothing:antialiased;overflow-x:hidden}}
.wrap{{max-width:1140px;margin:0 auto;padding:0 clamp(.9rem,3vw,1.25rem)}}
nav{{position:fixed;inset:0 0 auto;z-index:100;background:rgba(44,51,57,.95);backdrop-filter:blur(12px);border-bottom:3px solid var(--orange)}}
nav .wrap{{height:64px;display:flex;align-items:center;justify-content:space-between;gap:1rem}}
.brand{{display:flex;align-items:center;gap:.65rem}}
.brand img{{height:40px}}
.brand b{{color:#fff;font-size:.88rem;display:block}}
.brand span{{color:rgba(255,255,255,.68);font-size:.7rem}}
.nav-links{{display:flex;gap:.15rem;flex-wrap:wrap}}
.nav-links a{{color:rgba(255,255,255,.75);text-decoration:none;font-size:.78rem;font-weight:500;padding:.35rem .5rem;border-radius:6px}}
.nav-links a:hover,.nav-links a.on{{color:#fff;background:rgba(255,255,255,.12)}}
.menu{{display:none;background:transparent;border:1px solid rgba(255,255,255,.3);color:#fff;padding:.35rem .6rem;border-radius:6px}}

/* HERO + animated “video-like” background */
.hero{{min-height:92vh;display:grid;place-items:end stretch;position:relative;overflow:hidden;color:#fff}}
.hero-media{{
  position:absolute;inset:-8%;
  background:url("media/hero-data.jpg") center/cover no-repeat;
  animation:drift 22s ease-in-out infinite alternate;
  will-change:transform;
}}
.hero-scan{{
  position:absolute;inset:0;pointer-events:none;opacity:.35;
  background:repeating-linear-gradient(180deg,transparent 0 3px,rgba(0,179,175,.07) 3px 4px);
  animation:scan 8s linear infinite;
}}
.hero-glow{{
  position:absolute;width:55%;height:55%;border-radius:50%;filter:blur(60px);opacity:.35;
  background:radial-gradient(circle,rgba(0,179,175,.55),transparent 70%);
  top:10%;right:5%;animation:pulse 7s ease-in-out infinite alternate;
}}
.hero-glow2{{
  position:absolute;width:40%;height:40%;border-radius:50%;filter:blur(50px);opacity:.28;
  background:radial-gradient(circle,rgba(243,154,26,.5),transparent 70%);
  bottom:5%;left:0;animation:pulse 9s ease-in-out infinite alternate-reverse;
}}
@keyframes drift{{from{{transform:scale(1.05) translate(0,0)}}to{{transform:scale(1.18) translate(-3%,2%)}}}}
@keyframes scan{{from{{transform:translateY(-8%)}}to{{transform:translateY(8%)}}}}
@keyframes pulse{{from{{opacity:.2;transform:scale(.95)}}to{{opacity:.42;transform:scale(1.08)}}}}
.hero-scrim{{
  position:absolute;inset:0;
  background:linear-gradient(115deg,rgba(21,28,34,.93) 0%,rgba(21,28,34,.72) 48%,rgba(21,28,34,.4) 100%),
             linear-gradient(180deg,rgba(21,28,34,.2),rgba(21,28,34,.88));
}}
.hero-inner{{position:relative;z-index:1;padding:8.5rem 0 3.5rem;width:100%}}
.chip{{display:inline-flex;align-items:center;gap:.45rem;background:rgba(243,154,26,.18);border:1px solid rgba(243,154,26,.4);color:#ffc56f;font-size:.78rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase;padding:.4rem .8rem;border-radius:999px;margin-bottom:1.1rem}}
.chip i{{width:8px;height:8px;border-radius:50%;background:var(--orange);animation:pulse 1.6s ease-in-out infinite}}
.hero h1{{font-family:var(--display);font-weight:800;letter-spacing:-.03em;font-size:clamp(2.4rem,5vw,3.7rem);line-height:1.08;max-width:15ch;margin-bottom:1rem;text-shadow:0 2px 20px rgba(0,0,0,.35)}}
.hero h1 em{{font-style:normal;color:var(--orange)}}
.hero-lead{{font-size:1.12rem;color:rgba(255,255,255,.9);margin-bottom:.85rem;font-weight:500}}
.hero-obj{{font-size:1.08rem;color:rgba(255,255,255,.84);max-width:52ch;line-height:1.55;margin-bottom:2rem;border-left:3px solid var(--orange);padding-left:1rem}}
.hero-metrics{{display:grid;grid-template-columns:repeat(4,minmax(0,150px));gap:.7rem}}
.metric{{background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.2);backdrop-filter:blur(10px);border-radius:var(--r);padding:1rem .85rem}}
.metric b{{display:block;font-family:var(--display);font-size:1.85rem;color:var(--orange);line-height:1}}
.metric span{{font-size:.8rem;color:rgba(255,255,255,.82)}}

section{{padding:4.5rem 0}}
.section-alt{{background:linear-gradient(180deg,var(--alt),var(--bg))}}
.kicker{{color:var(--teal);font-size:.8rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;margin-bottom:.45rem}}
h2{{font-family:var(--display);font-size:clamp(1.7rem,2.8vw,2.2rem);letter-spacing:-.02em;color:var(--charcoal);margin-bottom:.4rem}}
.sub{{color:var(--mute);font-size:1.02rem;max-width:54ch;margin-bottom:1.6rem}}

.bento{{display:grid;gap:.85rem}}
.bento-4{{grid-template-columns:repeat(4,1fr)}}
.bento-3{{grid-template-columns:repeat(3,1fr)}}
.card{{background:var(--surface);border:1px solid var(--line);border-radius:var(--r);padding:1.2rem 1.1rem;box-shadow:var(--shadow);transition:.2s}}
.card:hover{{transform:translateY(-2px);border-color:rgba(0,179,175,.35)}}
.card .glyph{{width:42px;height:42px;border-radius:10px;display:grid;place-items:center;background:linear-gradient(145deg,rgba(0,179,175,.15),rgba(243,154,26,.1));color:var(--teal-deep);font-family:var(--display);font-weight:800;margin-bottom:.65rem}}
.card h3{{font-family:var(--display);font-size:1.05rem;margin-bottom:.3rem}}
.card p{{font-size:.92rem;color:var(--mute)}}
.obj-card{{cursor:pointer;text-align:left;font:inherit;color:inherit;width:100%}}
.obj-card.on{{border-top:3px solid var(--orange)}}
.obj-panel{{margin-top:1rem;background:var(--surface);border:1px solid var(--line);border-left:4px solid var(--teal);border-radius:var(--r);padding:1.1rem 1.25rem}}
.obj-panel strong{{display:block;font-family:var(--display);font-size:1.1rem;margin-bottom:.3rem}}
.obj-panel p{{font-size:1rem;color:var(--mute)}}

/* FLOW full width, no crop */
.flow-shell{{background:var(--surface);border:1px solid var(--line);border-radius:16px;box-shadow:var(--shadow);overflow:hidden}}
.flow-bar{{display:flex;justify-content:space-between;gap:.75rem;flex-wrap:wrap;padding:.75rem 1rem;border-bottom:1px solid var(--line);background:var(--alt);font-size:.85rem;color:var(--mute)}}
.flow-legend{{display:flex;gap:.85rem;flex-wrap:wrap}}
.flow-legend span{{display:inline-flex;align-items:center;gap:.35rem}}
.dot{{width:10px;height:10px;border-radius:3px}}
.flow-canvas{{width:100%;padding:.5rem .75rem 0;background:linear-gradient(180deg,#fbfdff,#eef4fc);overflow-x:auto;-webkit-overflow-scrolling:touch}}
#diagrama{{width:100%;height:auto;display:block;max-height:min(42vh,380px);min-width:0}}
.flecha{{fill:none;stroke:#7f93a6;stroke-width:1.6;opacity:.8}}
.flecha.ciclo{{stroke:var(--orange);stroke-dasharray:6 4;opacity:.75}}
.lbl-ciclo{{fill:var(--orange);font-size:11px;font-weight:700;text-anchor:middle;font-family:Inter,sans-serif}}
.nodo{{cursor:pointer}}
.nodo .caja{{stroke:var(--charcoal);stroke-width:1.4;transition:.15s}}
.nodo:hover .caja,.nodo.activo .caja{{stroke:var(--teal);stroke-width:2.4;filter:drop-shadow(0 4px 10px rgba(0,179,175,.25))}}
.nodo.activo .caja{{stroke:var(--orange)}}
.caja-entrada{{fill:#dff7f6}}.caja-proceso{{fill:#fff}}.caja-dato{{fill:#eef7e8}}.caja-salida{{fill:#fff4e5}}
.badge{{fill:var(--charcoal)}}.nodo.activo .badge{{fill:var(--orange)}}
.badge-n{{fill:#fff;font-size:9px;font-weight:700;text-anchor:middle;font-family:Inter,sans-serif}}
.fase{{fill:var(--mute);font-size:7.5px;font-weight:700;text-anchor:middle;text-transform:uppercase;font-family:Inter,sans-serif}}
.tit{{fill:var(--charcoal);font-size:11px;font-weight:700;text-anchor:middle;font-family:Inter,sans-serif}}
.flow-detail{{display:grid;grid-template-columns:56px 1fr;gap:.9rem;padding:1rem 1.15rem 1.2rem;border-top:1px solid var(--line)}}
.flow-step{{width:52px;height:52px;border-radius:12px;background:var(--charcoal);color:#fff;display:grid;place-items:center;font-family:var(--display);font-weight:800;font-size:1.2rem}}
.flow-detail h3{{font-family:var(--display);font-size:1.2rem;margin-bottom:.2rem}}
.flow-detail .proceso{{font-size:.98rem;margin-bottom:.7rem;font-weight:500}}
.flow-grid{{display:grid;grid-template-columns:1.2fr 1fr 1fr;gap:.65rem}}
.flow-box{{background:var(--alt);border-radius:10px;padding:.7rem .85rem;border:1px solid var(--line)}}
.flow-box h4{{font-size:.72rem;text-transform:uppercase;letter-spacing:.05em;color:var(--teal-deep);margin-bottom:.3rem}}
.flow-box ul{{margin-left:1rem;font-size:.88rem;color:var(--mute)}}
.flow-box p{{font-size:.88rem;color:var(--mute)}}

.plan{{display:grid;grid-template-columns:repeat(3,1fr);gap:.85rem}}
.plan-col{{background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:1.15rem;box-shadow:var(--shadow)}}
.plan-col header{{display:flex;align-items:center;gap:.65rem;margin-bottom:.8rem}}
.plan-col .ph{{width:42px;height:42px;border-radius:50%;background:var(--charcoal);color:#fff;display:grid;place-items:center;font-family:var(--display);font-weight:800;border:3px solid var(--orange);font-size:.9rem}}
.plan-col h3{{font-family:var(--display);font-size:1.1rem}}
.plan-col ul{{list-style:none;display:grid;gap:.35rem}}
.plan-col li{{font-size:.9rem;color:var(--mute);padding:.5rem .65rem;background:var(--alt);border-radius:8px;border-left:3px solid var(--teal)}}

.split{{display:grid;grid-template-columns:1fr 1fr;gap:.85rem}}
.know{{border-radius:14px;padding:1.4rem;color:#fff}}
.know.ex{{background:linear-gradient(145deg,#006a67,#00B3AF)}}
.know.ta{{background:linear-gradient(145deg,#875200,#F39A1A)}}
.know h3{{font-family:var(--display);font-size:1.25rem;margin-bottom:.7rem}}
.know ul{{list-style:none;display:grid;gap:.4rem}}
.know li{{font-size:.95rem;background:rgba(255,255,255,.14);padding:.65rem .8rem;border-radius:10px}}

.canal-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:.45rem}}
.canal-grid button{{border:1px solid var(--line);background:var(--surface);color:var(--ink);font:600 .88rem var(--font);padding:.7rem .8rem;border-radius:10px;cursor:pointer;text-align:left}}
.canal-grid button:hover,.canal-grid button.on{{background:var(--charcoal);color:#fff}}

.servicios{{display:grid;grid-template-columns:repeat(4,1fr);gap:.65rem}}
.svc{{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:1rem;text-align:left;font:inherit;color:inherit;cursor:pointer;box-shadow:var(--shadow)}}
.svc:hover,.svc.on{{border-left:3px solid var(--orange)}}
.svc b{{display:block;font-family:var(--display);font-size:1rem;margin-bottom:.25rem}}
.svc span{{font-size:.85rem;color:var(--mute)}}

/* VIZ Valor Plan Canales Servicios */
.valor-stage{{display:grid;grid-template-columns:1.05fr .95fr;gap:1.1rem;margin-top:1.4rem}}
.pillar-stack{{display:grid;gap:.7rem}}
.pillar-btn{{display:grid;grid-template-columns:56px 1fr;gap:.9rem;align-items:center;width:100%;text-align:left;font:inherit;color:inherit;cursor:pointer;border:1px solid var(--line);background:var(--surface);border-radius:16px;padding:1rem 1.1rem;box-shadow:var(--shadow);transition:.25s;position:relative;overflow:hidden}}
.pillar-btn::before{{content:"";position:absolute;left:0;top:0;bottom:0;width:4px;background:var(--teal);transform:scaleY(0);transition:.25s}}
.pillar-btn:hover,.pillar-btn.on{{transform:translateX(4px);border-color:rgba(0,179,175,.4)}}
.pillar-btn.on{{background:var(--charcoal);color:#fff}}
.pillar-btn.on::before{{transform:scaleY(1);background:var(--orange)}}
.pillar-btn.on p{{color:rgba(255,255,255,.72)}}
.pillar-ico{{width:56px;height:56px;border-radius:14px;display:grid;place-items:center;background:linear-gradient(145deg,rgba(0,179,175,.18),rgba(243,154,26,.12));font-family:var(--display);font-weight:800;font-size:1.2rem;color:var(--teal-deep)}}
.pillar-btn.on .pillar-ico{{background:rgba(243,154,26,.2);color:var(--orange)}}
.pillar-btn h3{{font-family:var(--display);font-size:1.15rem;margin-bottom:.2rem}}
.pillar-btn p{{font-size:.92rem;color:var(--mute);margin:0}}
.valor-panel{{background:linear-gradient(160deg,var(--charcoal),#1a3338);color:#fff;border-radius:18px;padding:1.6rem 1.5rem;border-top:4px solid var(--orange);display:flex;flex-direction:column;justify-content:center;min-height:220px}}
.valor-panel .eyebrow{{color:var(--orange);font-size:.75rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;margin-bottom:.5rem}}
.valor-panel h3{{font-family:var(--display);font-size:1.45rem;margin-bottom:.55rem}}
.valor-panel p{{color:rgba(255,255,255,.78);font-size:1.02rem}}
.adv-rail{{display:grid;grid-template-columns:repeat(7,1fr);gap:.55rem;margin-top:1.1rem}}
.adv-chip{{border:1px solid var(--line);background:var(--surface);border-radius:14px;padding:1rem .65rem;cursor:pointer;text-align:center;font:inherit;color:inherit;transition:.25s;box-shadow:var(--shadow);min-height:110px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:.45rem}}
.adv-chip:hover,.adv-chip.on{{background:var(--charcoal);color:#fff;transform:translateY(-4px);border-color:var(--charcoal)}}
.adv-chip .av{{width:36px;height:36px;border-radius:50%;display:grid;place-items:center;background:rgba(0,179,175,.15);color:var(--teal-deep);font-family:var(--display);font-weight:800;font-size:.85rem}}
.adv-chip.on .av{{background:rgba(243,154,26,.25);color:var(--orange)}}
.adv-chip b{{font-family:var(--display);font-size:.82rem;line-height:1.2}}
.adv-chip span{{font-size:.72rem;color:var(--mute);line-height:1.25}}
.adv-chip.on span{{color:rgba(255,255,255,.7)}}
.adv-spotlight{{margin-top:.85rem;background:var(--surface);border:1px solid var(--line);border-left:4px solid var(--teal);border-radius:12px;padding:1rem 1.2rem;display:none}}
.adv-spotlight.show{{display:block;animation:fadeUp .3s ease}}
@keyframes fadeUp{{from{{opacity:0;transform:translateY(6px)}}to{{opacity:1;transform:none}}}}
.roadmap{{margin-top:1.5rem}}
.roadmap-track{{display:grid;grid-template-columns:repeat(3,1fr);gap:0;position:relative}}
.roadmap-track::before{{content:"";position:absolute;top:28px;left:12%;right:12%;height:3px;background:linear-gradient(90deg,var(--teal),var(--orange));opacity:.35;z-index:0}}
.road-step{{position:relative;z-index:1;background:transparent;border:none;cursor:pointer;padding:0 .4rem;text-align:center;font:inherit;color:inherit}}
.road-dot{{width:56px;height:56px;border-radius:50%;margin:0 auto .85rem;display:grid;place-items:center;background:var(--surface);border:3px solid var(--teal);font-family:var(--display);font-weight:800;color:var(--charcoal);box-shadow:var(--shadow);transition:.25s}}
.road-step:hover .road-dot,.road-step.on .road-dot{{background:var(--charcoal);color:#fff;border-color:var(--orange);transform:scale(1.08)}}
.road-step h3{{font-family:var(--display);font-size:1.15rem;margin-bottom:.25rem}}
.road-step .hint{{font-size:.82rem;color:var(--mute)}}
.road-panel{{margin-top:1.25rem;background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:1.35rem 1.4rem;box-shadow:var(--shadow);display:grid;grid-template-columns:auto 1fr;gap:1.1rem}}
.road-badge{{width:64px;height:64px;border-radius:16px;background:var(--charcoal);color:#fff;display:grid;place-items:center;font-family:var(--display);font-weight:800;font-size:1.2rem;border-bottom:4px solid var(--orange)}}
.road-panel h3{{font-family:var(--display);font-size:1.25rem;margin-bottom:.75rem}}
.road-items{{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:.5rem;list-style:none;padding:0}}
.road-items li{{font-size:.92rem;color:var(--mute);padding:.7rem .85rem;background:var(--alt);border-radius:10px;border-left:3px solid var(--teal);opacity:0;transform:translateY(8px);animation:fadeUp .35s ease forwards}}
.canal-stage{{display:grid;grid-template-columns:260px 1fr;gap:1.25rem;margin-top:1.4rem;align-items:center}}
.canal-hub{{aspect-ratio:1;border-radius:50%;background:var(--charcoal);color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:1.4rem;border:4px solid var(--orange);box-shadow:0 0 0 12px rgba(243,154,26,.08),var(--shadow);position:relative;overflow:hidden}}
.canal-hub::before{{content:"";position:absolute;inset:16%;border:1px dashed rgba(0,179,175,.35);border-radius:50%;animation:spinSlow 24s linear infinite}}
@keyframes spinSlow{{to{{transform:rotate(360deg)}}}}
.canal-hub .hub-label{{font-size:.7rem;letter-spacing:.1em;text-transform:uppercase;color:var(--orange);font-weight:700;margin-bottom:.4rem;position:relative}}
.canal-hub h3{{font-family:var(--display);font-size:1.15rem;position:relative;line-height:1.25;margin-bottom:.35rem}}
.canal-hub p{{font-size:.86rem;color:rgba(255,255,255,.72);position:relative}}
.canal-mosaic{{display:grid;grid-template-columns:repeat(4,1fr);gap:.55rem}}
.canal-tile{{aspect-ratio:1.05;border:1px solid var(--line);background:var(--surface);border-radius:14px;cursor:pointer;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:.45rem;font:inherit;color:inherit;transition:.25s;box-shadow:var(--shadow);padding:.55rem}}
.canal-tile:hover,.canal-tile.on{{background:linear-gradient(160deg,var(--charcoal),#163d3c);color:#fff;transform:translateY(-3px);border-color:transparent}}
.canal-tile .ci{{width:38px;height:38px;border-radius:11px;display:grid;place-items:center;background:linear-gradient(145deg,rgba(0,179,175,.16),rgba(243,154,26,.12));font-family:var(--display);font-weight:800;font-size:.85rem;color:var(--teal-deep)}}
.canal-tile.on .ci{{background:rgba(243,154,26,.25);color:var(--orange)}}
.canal-tile b{{font-family:var(--display);font-size:.8rem;text-align:center;line-height:1.2}}
.svc-mosaic{{display:grid;grid-template-columns:repeat(4,1fr);gap:.7rem;margin-top:1.3rem}}
.svc-tile{{position:relative;overflow:hidden;border:1px solid var(--line);background:var(--surface);border-radius:16px;padding:1.15rem;cursor:pointer;text-align:left;font:inherit;color:inherit;transition:.3s;box-shadow:var(--shadow);display:flex;flex-direction:column;justify-content:flex-end;min-height:138px}}
.svc-tile::after{{content:"";position:absolute;inset:auto -30% -50%;height:80%;background:radial-gradient(circle,rgba(0,179,175,.2),transparent 65%);transition:.35s}}
.svc-tile:nth-child(1),.svc-tile:nth-child(6){{grid-column:span 2;min-height:158px;background:linear-gradient(145deg,#2C3339,#006a67);color:#fff;border:none}}
.svc-tile:nth-child(1) span,.svc-tile:nth-child(6) span{{color:rgba(255,255,255,.75)}}
.svc-tile:nth-child(1) .sn,.svc-tile:nth-child(6) .sn{{color:var(--orange)}}
.svc-tile:hover,.svc-tile.on{{transform:translateY(-4px)}}
.svc-tile.on{{outline:2px solid var(--orange)}}
.svc-tile .sn{{position:relative;z-index:1;font-size:.68rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--teal);margin-bottom:.4rem}}
.svc-tile b{{position:relative;z-index:1;font-family:var(--display);font-size:1.1rem;margin-bottom:.25rem}}
.svc-tile span{{position:relative;z-index:1;font-size:.88rem;color:var(--mute)}}
.svc-detail{{margin-top:.85rem;padding:1rem 1.15rem;background:var(--alt);border-radius:12px;border-left:4px solid var(--orange);font-size:1rem;color:var(--mute);display:none}}
.svc-detail.show{{display:block;animation:fadeUp .3s ease}}

/* Problematica + Ventajas PDI */
.prob-stage{{display:grid;grid-template-columns:1fr 1.05fr;gap:1.1rem;margin-top:1.4rem;align-items:start}}
.prob-list{{display:grid;gap:.55rem}}
.prob-btn{{
  width:100%;text-align:left;font:inherit;color:inherit;cursor:pointer;border:1px solid var(--line);
  background:var(--surface);border-radius:14px;padding:.95rem 1rem;display:grid;grid-template-columns:48px 1fr;gap:.75rem;align-items:center;
  box-shadow:var(--shadow);transition:.22s;position:relative;overflow:hidden;
}}
.prob-btn::before{{content:"";position:absolute;left:0;top:0;bottom:0;width:4px;background:var(--orange);transform:scaleY(0);transition:.22s}}
.prob-btn.solucion::before{{background:var(--teal)}}
.prob-btn:hover,.prob-btn.on{{transform:translateX(3px);border-color:rgba(0,179,175,.35)}}
.prob-btn.on{{background:var(--charcoal);color:#fff}}
.prob-btn.on::before{{transform:scaleY(1)}}
.prob-btn.on .prob-meta{{color:rgba(255,255,255,.7)}}
.prob-id{{width:48px;height:48px;border-radius:12px;display:grid;place-items:center;font-family:var(--display);font-weight:800;background:rgba(243,154,26,.15);color:var(--primary)}}
.prob-btn.solucion .prob-id{{background:rgba(0,179,175,.15);color:var(--teal-deep)}}
.prob-btn.on .prob-id{{background:rgba(243,154,26,.25);color:var(--orange)}}
.prob-btn h3{{font-family:var(--display);font-size:1.02rem;margin-bottom:.15rem}}
.prob-meta{{font-size:.82rem;color:var(--mute)}}
.prob-panel{{
  background:var(--surface);border:1px solid var(--line);border-radius:18px;padding:1.4rem 1.35rem;box-shadow:var(--shadow);
  border-top:4px solid var(--orange);min-height:280px;
}}
.prob-panel.solucion{{border-top-color:var(--teal)}}
.prob-panel .tag{{display:inline-block;font-size:.72rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--orange);margin-bottom:.55rem}}
.prob-panel.solucion .tag{{color:var(--teal-deep)}}
.prob-panel h3{{font-family:var(--display);font-size:1.35rem;margin-bottom:.55rem}}
.prob-panel p{{font-size:.98rem;color:var(--mute);margin-bottom:.75rem}}
.prob-panel .efecto{{background:var(--alt);border-radius:12px;padding:.85rem 1rem;border-left:3px solid var(--teal);font-size:.95rem;color:var(--ink)}}
.ctx-bar{{display:flex;flex-wrap:wrap;gap:.45rem;margin-top:1rem}}
.ctx-bar span{{font-size:.8rem;background:var(--surface);border:1px solid var(--line);border-radius:999px;padding:.35rem .75rem;color:var(--mute);font-weight:500}}
.pdi-stage{{margin-top:1.4rem}}
.pdi-tabs{{display:grid;grid-template-columns:repeat(4,1fr);gap:.55rem;margin-bottom:1rem}}
.pdi-tab{{
  border:1px solid var(--line);background:var(--surface);border-radius:14px;padding:1rem .85rem;cursor:pointer;
  text-align:left;font:inherit;color:inherit;transition:.22s;box-shadow:var(--shadow);min-height:108px;
}}
.pdi-tab:hover,.pdi-tab.on{{background:var(--charcoal);color:#fff;border-color:var(--charcoal);transform:translateY(-2px)}}
.pdi-tab .ln{{font-size:.72rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--teal);margin-bottom:.35rem}}
.pdi-tab.on .ln{{color:var(--orange)}}
.pdi-tab h3{{font-family:var(--display);font-size:.95rem;line-height:1.25;margin-bottom:.3rem}}
.pdi-tab p{{font-size:.8rem;color:var(--mute);margin:0}}
.pdi-tab.on p{{color:rgba(255,255,255,.7)}}
.pdi-panel{{background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:1.35rem;box-shadow:var(--shadow)}}
.pdi-panel h3{{font-family:var(--display);font-size:1.3rem;margin-bottom:.35rem}}
.pdi-panel .foco{{color:var(--mute);font-size:.95rem;margin-bottom:1rem}}
.pdi-inds{{display:grid;grid-template-columns:repeat(2,1fr);gap:.65rem;list-style:none;padding:0;margin:0}}
.pdi-inds li{{background:var(--alt);border-radius:12px;padding:1rem;border-top:3px solid var(--teal);opacity:0;transform:translateY(8px);animation:fadeUp .35s ease forwards}}
.pdi-inds li:nth-child(2),.pdi-inds li:nth-child(4){{border-top-color:var(--orange)}}
.pdi-inds b{{display:block;font-family:var(--display);font-size:.98rem;margin-bottom:.3rem;color:var(--charcoal)}}
.pdi-inds span{{font-size:.88rem;color:var(--mute)}}

/* KPIs */
.kpi-tabs{{display:flex;gap:.4rem;flex-wrap:wrap;margin-bottom:1.1rem}}
.kpi-tab{{border:1px solid var(--line);background:var(--surface);color:var(--mute);padding:.45rem .85rem;border-radius:999px;cursor:pointer;font:600 .85rem var(--font)}}
.kpi-tab.on{{background:var(--teal);color:#fff;border-color:var(--teal)}}
.kpi-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:.65rem}}
.kpi{{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:1rem;box-shadow:var(--shadow);border-top:3px solid var(--teal);transition:.2s}}
.kpi[data-dim="roi"]{{border-top-color:var(--orange)}}
.kpi[data-dim="sostenibilidad"]{{border-top-color:var(--primary)}}
.kpi[data-dim="operativa"]{{border-top-color:var(--teal-deep)}}
.kpi:hover{{transform:translateY(-2px)}}
.kpi-top{{display:flex;justify-content:space-between;align-items:center;margin-bottom:.4rem}}
.kid{{font-size:.72rem;font-weight:700;color:var(--orange)}}
.kdim{{font-size:.68rem;color:var(--mute);text-transform:uppercase;letter-spacing:.04em}}
.kpi h4{{font-size:.95rem;font-family:var(--display);margin-bottom:.3rem;line-height:1.3}}
.kpi p{{font-size:.88rem;color:var(--teal-deep);font-weight:600}}

/* Hardware + budget */
.hw-grid{{display:grid;grid-template-columns:1fr 1fr;gap:.85rem;margin-bottom:1rem}}
.hw{{background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:1.25rem;box-shadow:var(--shadow)}}
.hw .tag{{display:inline-block;font-size:.7rem;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:var(--teal);background:rgba(0,179,175,.12);padding:.25rem .55rem;border-radius:6px;margin-bottom:.55rem}}
.hw.ups .tag{{color:var(--primary);background:rgba(243,154,26,.12)}}
.hw h3{{font-family:var(--display);font-size:1.15rem;margin-bottom:.65rem}}
.hw ul{{list-style:none;display:grid;gap:.35rem;margin-bottom:.75rem}}
.hw li{{font-size:.9rem;color:var(--mute);padding:.35rem 0;border-bottom:1px solid var(--line)}}
.hw .price{{font-family:var(--display);font-size:1.35rem;color:var(--primary);font-weight:800}}
.budget{{background:var(--charcoal);color:#fff;border-radius:16px;padding:1.5rem;border-top:4px solid var(--orange)}}
.budget .total{{font-family:var(--display);font-size:clamp(2rem,3vw,2.6rem);color:var(--orange);margin:.2rem 0 1rem}}
.budget-row{{display:grid;grid-template-columns:1fr auto auto;gap:.75rem;align-items:center;padding:.55rem 0;border-bottom:1px solid rgba(255,255,255,.1);font-size:.92rem}}
.budget-row:last-child{{border-bottom:none}}
.budget-row .bar{{height:6px;background:rgba(255,255,255,.12);border-radius:999px;overflow:hidden;margin-top:.35rem}}
.budget-row .fill{{height:100%;background:linear-gradient(90deg,var(--teal),var(--orange))}}

.lineas{{display:grid;grid-template-columns:repeat(3,1fr);gap:.85rem}}
.linea{{border-radius:14px;padding:1.4rem;color:#fff;min-height:120px}}
.linea:nth-child(1){{background:linear-gradient(150deg,#2C3339,#006a67)}}
.linea:nth-child(2){{background:linear-gradient(150deg,#2C3339,#875200)}}
.linea:nth-child(3){{background:linear-gradient(150deg,#2C3339,#00B3AF)}}
.linea h3{{font-family:var(--display);font-size:1.15rem;margin-bottom:.3rem}}
.linea p{{opacity:.8;font-size:.92rem}}

.estudios{{display:none}}
.tray-section{{padding:4.5rem 0 5rem;background:linear-gradient(165deg,#1a2228 0%,#2C3339 45%,#163d3c 100%);color:#fff;position:relative;overflow:hidden}}
.tray-section::before{{content:"";position:absolute;inset:auto -20% -40% 40%;height:70%;background:radial-gradient(circle,rgba(243,154,26,.22),transparent 60%);pointer-events:none}}
.tray-section::after{{content:"";position:absolute;top:0;left:0;right:0;height:4px;background:linear-gradient(90deg,var(--teal),var(--orange))}}
.tray-section .kicker{{color:var(--orange)}}
.tray-section h2{{color:#fff;font-size:clamp(1.9rem,3.4vw,2.8rem);max-width:16ch}}
.tray-section .sub{{color:rgba(255,255,255,.72);max-width:42rem}}
.tray-stats{{display:grid;grid-template-columns:repeat(4,1fr);gap:.7rem;margin:1.5rem 0 1.6rem}}
.tray-stat{{background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:14px;padding:1rem 1.05rem;backdrop-filter:blur(6px)}}
.tray-stat b{{display:block;font-family:var(--display);font-size:1.7rem;color:var(--orange);line-height:1.1}}
.tray-stat span{{font-size:.82rem;color:rgba(255,255,255,.68)}}
.tray-rail{{display:grid;grid-template-columns:repeat(7,minmax(0,1fr));gap:.45rem;margin-bottom:1.1rem}}
.tray-chip{{
  border:1px solid rgba(255,255,255,.14);background:rgba(255,255,255,.05);color:#fff;border-radius:14px;
  padding:.85rem .6rem;cursor:pointer;text-align:left;font:inherit;transition:.25s;min-height:92px;
}}
.tray-chip:hover,.tray-chip.on{{background:#fff;color:var(--charcoal);transform:translateY(-3px);border-color:#fff}}
.tray-chip .n{{display:block;font-size:.7rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--teal);margin-bottom:.25rem}}
.tray-chip.on .n{{color:var(--orange)}}
.tray-chip b{{display:block;font-family:var(--display);font-size:.86rem;line-height:1.2;margin-bottom:.2rem}}
.tray-chip span{{font-size:.72rem;color:rgba(255,255,255,.6);line-height:1.25}}
.tray-chip.on span{{color:var(--mute)}}
.tray-stage{{display:grid;grid-template-columns:1.15fr .85fr;gap:1rem;align-items:stretch}}
.tray-preview{{
  position:relative;border-radius:18px;overflow:hidden;min-height:380px;background:#0f1418;
  border:1px solid rgba(255,255,255,.12);box-shadow:0 20px 50px rgba(0,0,0,.35);
}}
.tray-preview iframe{{width:100%;height:100%;min-height:380px;border:0;background:#fff}}
.tray-fallback{{
  position:absolute;inset:0;display:flex;flex-direction:column;align-items:flex-start;justify-content:flex-end;
  padding:1.5rem;background:
    linear-gradient(180deg,rgba(15,20,24,.15),rgba(15,20,24,.92)),
    radial-gradient(circle at 80% 20%,rgba(0,179,175,.35),transparent 45%),
    radial-gradient(circle at 20% 80%,rgba(243,154,26,.3),transparent 40%);
}}
.tray-fallback .badge{{font-size:.72rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--orange);margin-bottom:.55rem}}
.tray-fallback h3{{font-family:var(--display);font-size:1.45rem;margin-bottom:.4rem}}
.tray-fallback p{{color:rgba(255,255,255,.75);font-size:.95rem;margin-bottom:1rem;max-width:34ch}}
.tray-fallback a,.tray-ev a,.tray-side a.cta-ev{{
  display:inline-flex;align-items:center;gap:.4rem;background:var(--orange);color:#1a2228;font-weight:700;
  text-decoration:none;border-radius:999px;padding:.65rem 1.05rem;font-size:.9rem;
}}
.tray-side{{
  background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12);border-radius:18px;padding:1.35rem 1.3rem;
  display:flex;flex-direction:column;gap:.75rem;
}}
.tray-side .tag{{display:inline-block;font-size:.72rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--teal)}}
.tray-side h3{{font-family:var(--display);font-size:1.45rem;line-height:1.2}}
.tray-side .metric-row{{display:flex;align-items:baseline;gap:.55rem}}
.tray-side .metric-row b{{font-family:var(--display);font-size:2.4rem;color:var(--orange);line-height:1}}
.tray-side .metric-row span{{color:rgba(255,255,255,.65);font-size:.9rem}}
.tray-side p{{color:rgba(255,255,255,.75);font-size:.95rem}}
.tray-ev{{display:grid;gap:.45rem;margin-top:.35rem}}
.tray-ev button,.tray-ev a.chip{{
  width:100%;text-align:left;border:1px solid rgba(255,255,255,.14);background:rgba(255,255,255,.05);
  color:#fff;border-radius:12px;padding:.7rem .85rem;cursor:pointer;font:inherit;display:flex;justify-content:space-between;gap:.5rem;align-items:center;text-decoration:none;
}}
.tray-ev button:hover,.tray-ev button.on,.tray-ev a.chip:hover{{background:#fff;color:var(--charcoal)}}
.tray-ev .kind{{font-size:.68rem;font-weight:700;letter-spacing:.05em;text-transform:uppercase;opacity:.7}}
@media(max-width:1100px){{
  .tray-rail{{grid-template-columns:repeat(4,minmax(0,1fr))}}
  .tray-stats{{grid-template-columns:1fr 1fr}}
  .nav-links a{{font-size:.72rem;padding:.3rem .4rem}}
}}
@media(max-width:1000px){{
  .valor-stage,.roadmap-track,.canal-stage,.svc-mosaic,.canal-mosaic,.prob-stage,.pdi-inds,
  .bento-4,.bento-3,.plan,.split,.lineas,.piloto,.hero-metrics,.flow-grid,.servicios,.hw-grid,
  .adv-rail{{grid-template-columns:1fr 1fr}}
  .pdi-tabs{{grid-template-columns:1fr 1fr}}
  .svc-tile:nth-child(1),.svc-tile:nth-child(6){{grid-column:span 1}}
  .canal-mosaic{{grid-template-columns:repeat(3,1fr)}}
  .roadmap-track::before{{display:none}}
  .servicios{{grid-template-columns:1fr 1fr}}
  .budget-row{{grid-template-columns:1fr auto;gap:.4rem .75rem}}
  .budget-row span{{grid-column:2;justify-self:end}}
}}
@media(max-width:900px){{
  .nav-links{{display:none;position:absolute;top:64px;left:0;right:0;background:var(--charcoal);padding:.85rem 1rem 1.1rem;flex-direction:column;gap:.15rem;border-bottom:3px solid var(--orange);max-height:calc(100vh - 64px);overflow-y:auto}}
  .nav-links.open{{display:flex}}
  .nav-links a{{font-size:.95rem;padding:.7rem .75rem}}
  .menu{{display:inline-flex;align-items:center;gap:.35rem;cursor:pointer;font:600 .85rem var(--font)}}
  .tray-stage{{grid-template-columns:1fr}}
  .tray-rail{{
    display:flex;grid-template-columns:none;overflow-x:auto;gap:.5rem;padding-bottom:.55rem;
    scroll-snap-type:x mandatory;-webkit-overflow-scrolling:touch;
  }}
  .tray-chip{{min-width:158px;flex:0 0 158px;scroll-snap-align:start;min-height:88px}}
  .tray-preview,.tray-preview iframe{{min-height:280px}}
  .prob-stage{{grid-template-columns:1fr}}
  .adv-rail{{
    display:flex;grid-template-columns:none;overflow-x:auto;gap:.5rem;padding-bottom:.4rem;
    scroll-snap-type:x mandatory;-webkit-overflow-scrolling:touch;
  }}
  .adv-chip{{min-width:120px;flex:0 0 120px;scroll-snap-align:start}}
}}
@media(max-width:700px){{
  body{{font-size:16px}}
  .bento-4,.bento-3,.plan,.split,.lineas,.piloto,.hero-metrics,.flow-grid,.servicios,.hw-grid,
  .pdi-tabs,.pdi-inds,.canal-stage,.canal-mosaic,.svc-mosaic,.valor-stage,.roadmap-track,.road-panel,
  .prob-stage,.tray-stats{{grid-template-columns:1fr}}
  .hero{{min-height:auto}}
  .hero-inner{{padding:6.5rem 0 2.4rem}}
  .hero h1{{max-width:none;font-size:clamp(1.75rem,8vw,2.4rem)}}
  .hero-metrics{{grid-template-columns:1fr 1fr;max-width:100%}}
  .metric{{padding:.85rem .7rem}}
  .metric b{{font-size:1.45rem}}
  .hero-obj{{font-size:1rem;margin-bottom:1.4rem}}
  .section-alt,section{{padding-top:3.2rem;padding-bottom:3.2rem}}
  .flow-detail{{grid-template-columns:1fr}}
  .flow-bar{{font-size:.78rem}}
  #diagrama{{max-height:none;min-width:780px}}
  .flow-canvas{{padding-bottom:.5rem}}
  .budget{{padding:1.15rem}}
  .budget .total{{font-size:clamp(1.6rem,8vw,2.2rem)}}
  .budget-row{{grid-template-columns:1fr;gap:.25rem}}
  .budget-row span,.budget-row strong{{justify-self:start}}
  .cta{{padding:3rem 0}}
  .cta blockquote{{padding:0 .25rem}}
  .tray-section{{padding:3.2rem 0 3.6rem}}
  .tray-stat b{{font-size:1.35rem}}
  .pdi-tab{{min-height:0}}
  .prob-panel{{min-height:0}}
  .canal-hub{{max-width:220px;margin:0 auto}}
  .marquee-track{{gap:1.25rem;animation-duration:36s}}
}}
@media(max-width:420px){{
  .hero-metrics{{gap:.45rem}}
  .brand b{{font-size:.9rem}}
  .brand span{{font-size:.68rem}}
  .tray-chip{{min-width:140px;flex-basis:140px}}
}}

.piloto{{display:grid;grid-template-columns:.8fr 1.2fr;gap:1rem}}
.piloto-visual{{border-radius:14px;min-height:200px;background:url("media/hero-data.jpg") center/cover;position:relative}}
.piloto-visual::after{{content:"PILOTO";position:absolute;left:1rem;bottom:1rem;font-family:var(--display);font-weight:800;color:#fff;letter-spacing:.08em;background:rgba(44,51,57,.8);padding:.4rem .7rem;border-radius:8px;border-left:3px solid var(--orange);font-size:.9rem}}
.piloto-copy{{border-radius:14px;background:var(--charcoal);color:#fff;padding:1.75rem;display:flex;flex-direction:column;justify-content:center}}
.piloto-copy h3{{font-family:var(--display);font-size:1.3rem;line-height:1.3;margin-bottom:.6rem}}
.piloto-copy p{{color:rgba(255,255,255,.75);font-size:.98rem}}

.cta{{padding:4.2rem 0;text-align:center;background:var(--charcoal);border-top:4px solid var(--orange)}}
.cta blockquote{{font-family:var(--display);font-size:clamp(1.3rem,2.4vw,1.75rem);color:#fff;max-width:22em;margin:0 auto;line-height:1.35}}
.cta strong{{color:var(--orange)}}
.cta cite{{display:block;margin-top:1rem;font-style:normal;font-size:1rem;color:rgba(255,255,255,.68);font-family:var(--font)}}

.progress{{position:fixed;top:64px;left:0;height:3px;width:0;z-index:101;background:linear-gradient(90deg,var(--teal),var(--orange))}}
.reveal{{opacity:0;transform:translateY(16px);transition:.5s}}.reveal.on{{opacity:1;transform:none}}
.marquee{{overflow:hidden;border-block:1px solid var(--line);background:var(--surface)}}
.marquee-track{{display:flex;gap:2rem;width:max-content;padding:.9rem 0;animation:marquee 28s linear infinite}}
.marquee-track span{{font-family:var(--display);font-weight:700;font-size:.9rem;color:var(--mute)}}
@keyframes marquee{{to{{transform:translateX(-50%)}}}}

</style>
</head>
<body>
<div class="progress" id="bar"></div>
<nav>
  <div class="wrap">
    <div class="brand">
      <img src="logo-colmayor-blanco.png" alt="Colmayor"/>
      <div><b>Observatorio CTi</b><span>CEITTO · Colmayor</span></div>
    </div>
    <button class="menu" id="menu" type="button">Menú</button>
    <div class="nav-links" id="links">
      <a href="#inicio">Inicio</a>
      <a href="#objetivos">Objetivos</a>
      <a href="#problema">Problemas</a>
      <a href="#ventajas-pdi">Ventajas PDI</a>
      <a href="#flujo">Flujo</a>
      <a href="#kpis">KPIs</a>
      <a href="#hardware">Hardware</a>
      <a href="#servicios">Servicios</a>
      <a href="#piloto">Piloto</a>
      <a href="#estudios">Trayectoria</a>
    </div>
  </div>
</nav>

<header class="hero" id="inicio">
  <div class="hero-media" aria-hidden="true"></div>
  <div class="hero-glow" aria-hidden="true"></div>
  <div class="hero-glow2" aria-hidden="true"></div>
  <div class="hero-scan" aria-hidden="true"></div>
  <div class="hero-scrim" aria-hidden="true"></div>
  <div class="hero-inner">
    <div class="wrap">
      <div class="chip"><i></i> Observatorio de Ciencia, Tecnología e Innovación</div>
      <h1>De datos del entorno a <em>decisión</em> estratégica</h1>
      <p class="hero-lead">Organizar · Cuantificar · Procesar · Disponer</p>
      <p class="hero-obj"><strong>Objetivo:</strong> {OBJETIVO_CLARO}</p>
      <div class="hero-metrics">
        <div class="metric"><b>4</b><span>Objetivos</span></div>
        <div class="metric"><b>10</b><span>Etapas</span></div>
        <div class="metric"><b>20</b><span>KPIs MVP</span></div>
        <div class="metric"><b>{round(PRESUPUESTO['total']/1_000_000, 1):g}M</b><span>Presupuesto MVP</span></div>
      </div>
    </div>
  </div>
</header>

<section id="objetivos">
  <div class="wrap reveal">
    <p class="kicker">Direccionamiento</p>
    <h2>Objetivos específicos</h2>
    <div class="bento bento-4" style="margin-top:1.4rem">
      {''.join(f'''<button class="card obj-card{' on' if i==0 else ''}" data-i="{i}" type="button">
        <div class="glyph">{o['n']}</div>
        <h3>{o['t']}</h3>
        <p>{o['s']}</p>
      </button>''' for i,o in enumerate(OBJ))}
    </div>
    <div class="obj-panel" id="objPanel"><strong>{OBJ[0]['t']}</strong><p>{OBJ[0]['d']}</p></div>
  </div>
</section>

<section class="section-alt" id="problema">
  <div class="wrap reveal">
    <p class="kicker">Problemática institucional</p>
    <h2>De reportes fragmentados a inteligencia accionable</h2>
    <p class="sub">Retos reales de Colmayor para calidad, planeación, investigación y extensión, leídos a la luz del Plan de Desarrollo 2024-2028.</p>
    <div class="prob-stage">
      <div class="prob-list" id="probList">
        {''.join(f'''<button class="prob-btn{' solucion' if p['tipo']=='solucion' else ''}{' on' if i==0 else ''}" type="button" data-i="{i}">
          <div class="prob-id">{p['id']}</div>
          <div><h3>{p['titulo']}</h3><p class="prob-meta">{p['colmayor']}</p></div>
        </button>''' for i,p in enumerate(PROBLEMAS))}
      </div>
      <aside class="prob-panel{' solucion' if PROBLEMAS[0]['tipo']=='solucion' else ''}" id="probPanel">
        <p class="tag">Contexto Colmayor</p>
        <h3>{PROBLEMAS[0]['titulo']}</h3>
        <p>{PROBLEMAS[0]['desc']}</p>
        <div class="efecto"><strong>Implicación:</strong> {PROBLEMAS[0]['efecto']}</div>
      </aside>
    </div>
  </div>
</section>

<section id="ventajas-pdi">
  <div class="wrap reveal">
    <p class="kicker">Alineación institucional</p>
    <h2>Ventajas de adoptar el Observatorio</h2>
    <p class="sub">Articulados a las cuatro líneas del Plan de Desarrollo 2024-2028: Avanzando en la innovación y la transformación de la educación.</p>
    <div class="pdi-stage">
      <div class="pdi-tabs" id="pdiTabs">
        {''.join(f'''<button class="pdi-tab{' on' if i==0 else ''}" type="button" data-i="{i}">
          <p class="ln">{v['linea']}</p>
          <h3>{v['nombre']}</h3>
          <p>{v['foco']}</p>
        </button>''' for i,v in enumerate(VENTAJAS_PDI))}
      </div>
      <div class="pdi-panel" id="pdiPanel">
        <h3>{VENTAJAS_PDI[0]['nombre']}</h3>
        <p class="foco">{VENTAJAS_PDI[0]['foco']}</p>
        <ul class="pdi-inds">
          {''.join(f'<li style="animation-delay:{i*0.05}s"><b>{ind["t"]}</b><span>{ind["m"]}</span></li>' for i,ind in enumerate(VENTAJAS_PDI[0]['indicadores']))}
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section-alt" id="valor">
  <div class="wrap reveal">
    <p class="kicker">Valor</p>
    <h2>Por qué un Observatorio CTi</h2>
    <div class="valor-stage">
      <div class="pillar-stack" id="pillarStack">
        {''.join(f'''<button class="pillar-btn{' on' if i==0 else ''}" type="button" data-i="{i}">
          <div class="pillar-ico">{i+1}</div>
          <div><h3>{p["t"]}</h3><p>{p["d"]}</p></div>
        </button>''' for i,p in enumerate(PILARES))}
      </div>
      <aside class="valor-panel" id="valorPanel">
        <p class="eyebrow">Pilar activo</p>
        <h3>{PILARES[0]["t"]}</h3>
        <p>{PILARES[0]["d"]}</p>
      </aside>
    </div>
    <div class="adv-rail" id="advRail">
      {''.join(f'''<button class="adv-chip" type="button" data-i="{i}">
        <span class="av">{i+1}</span><b>{v["t"]}</b><span>{v["d"]}</span>
      </button>''' for i,v in enumerate(VENTAJAS))}
    </div>
    <div class="adv-spotlight" id="advSpot"></div>
  </div>
</section>

<section id="flujo">
  <div class="wrap reveal">
    <p class="kicker">Operación</p>
    <h2>Diagrama de flujo del Observatorio CTi</h2>
    <p class="sub">Vista completa del ciclo. Clic en cada etapa para detalle del proceso.</p>
    <div class="flow-shell">
      <div class="flow-bar">
        <div class="flow-legend">
          <span><i class="dot" style="background:#dff7f6;border:1px solid #2C3339"></i>Entrada</span>
          <span><i class="dot" style="background:#eef7e8;border:1px solid #2C3339"></i>Captura</span>
          <span><i class="dot" style="background:#fff;border:1px solid #2C3339"></i>Proceso / análisis</span>
          <span><i class="dot" style="background:#fff4e5;border:1px solid #2C3339"></i>Salida / decisión</span>
        </div>
        <span>Clic en cada etapa</span>
      </div>
      <div class="flow-canvas">
        <svg id="diagrama" viewBox="0 0 1050 360" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <marker id="arrow" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7 Z" fill="#7f93a6"/></marker>
            <marker id="arrowC" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7 Z" fill="#F39A1A"/></marker>
          </defs>
          {''.join(edges_svg)}
          {''.join(nodes_svg)}
        </svg>
      </div>
      <div class="flow-detail" id="flowDetail">
        <div class="flow-step">{f0['n']}</div>
        <div>
          <h3>{f0['titulo']} · {f0['fase']}</h3>
          <p class="proceso">{f0['proceso']}</p>
          <div class="flow-grid">
            <div class="flow-box"><h4>Actividades</h4><ul>{''.join(f'<li>{a}</li>' for a in f0['actividades'])}</ul></div>
            <div class="flow-box"><h4>Entradas / salidas</h4><p><strong>En:</strong> {f0['entradas']}<br/><strong>Out:</strong> {f0['salidas']}</p></div>
            <div class="flow-box"><h4>Responsable</h4><p>{f0['responsable']}</p></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section-alt" id="plan">
  <div class="wrap reveal">
    <p class="kicker">2026-2</p>
    <h2>Plan de diseño</h2>
    <div class="roadmap">
      <div class="roadmap-track" id="roadTrack">
        {''.join(f'''<button class="road-step{' on' if i==0 else ''}" type="button" data-i="{i}">
          <div class="road-dot">{p["fase"]}</div>
          <h3>{p["t"]}</h3>
          <p class="hint">{len(p["items"])} actividades</p>
        </button>''' for i,p in enumerate(PLAN))}
      </div>
      <div class="road-panel" id="roadPanel">
        <div class="road-badge">{PLAN[0]["fase"]}</div>
        <div>
          <h3>{PLAN[0]["t"]}</h3>
          <ul class="road-items">{''.join(f'<li style="animation-delay:{i*0.05}s">{it}</li>' for i,it in enumerate(PLAN[0]["items"]))}</ul>
        </div>
      </div>
    </div>
  </div>
</section>

<section id="recoleccion">
  <div class="wrap reveal">
    <p class="kicker">Componentes</p>
    <h2>Recolección de información</h2>
    <div class="split" style="margin-top:1.3rem">
      <div class="know ex"><h3>Explícito</h3><ul><li>Fuentes secundarias VT/IC</li><li>Bases, patentes y convocatorias</li></ul></div>
      <div class="know ta"><h3>Tácito</h3><ul><li>Entrevistas a tomadores de decisión</li><li>Eventos, foros y observación directa</li></ul></div>
    </div>
  </div>
</section>

<section class="section-alt" id="kpis">
  <div class="wrap reveal">
    <p class="kicker">Indicadores MVP</p>
    <h2>20 KPIs en 4 dimensiones</h2>
    <p class="sub">Marco de gestión del observatorio: operativa, analítica, ROI y sostenibilidad.</p>
    <div class="kpi-tabs" id="kpiTabs">
      <button class="kpi-tab on" data-dim="all" type="button">Todos (20)</button>
      <button class="kpi-tab" data-dim="operativa" type="button">Operativa (4)</button>
      <button class="kpi-tab" data-dim="analitica" type="button">Analítica (5)</button>
      <button class="kpi-tab" data-dim="roi" type="button">ROI (8)</button>
      <button class="kpi-tab" data-dim="sostenibilidad" type="button">Sostenibilidad (3)</button>
    </div>
    <div class="kpi-grid" id="kpiGrid">{kpi_cards}</div>
  </div>
</section>

<section id="hardware">
  <div class="wrap reveal">
    <p class="kicker">Infraestructura MVP</p>
    <h2>Configuración recomendada y presupuesto MVP</h2>
    <p class="sub">{HW['ws']['titulo']} + {HW['ups']['titulo']} · inversión total del MVP.</p>
    <div class="hw-grid">
      <article class="hw">
        <span class="tag">Cotización jul-2026</span>
        <h3>{HW['ws']['titulo']}</h3>
        <ul>{''.join(f'<li>{s}</li>' for s in HW['ws']['specs'])}</ul>
        <div class="price">{fmt_cop(HW['ws']['cop'])}</div>
      </article>
      <article class="hw ups">
        <span class="tag">UPS</span>
        <h3>{HW['ups']['titulo']}</h3>
        <ul>{''.join(f'<li>{s}</li>' for s in HW['ups']['specs'])}</ul>
        <div class="price">{fmt_cop(HW['ups']['cop'])}</div>
      </article>
    </div>
    <div class="budget">
      <p style="font-size:.8rem;letter-spacing:.06em;text-transform:uppercase;opacity:.75">Presupuesto total del proyecto MVP</p>
      <div class="total">{fmt_cop(PRESUPUESTO['total'])}</div>
      {''.join(f'''<div class="budget-row">
        <div><div>{l['nombre']}</div><div class="bar"><div class="fill" style="width:{l['pct']}%"></div></div></div>
        <strong>{fmt_cop(l['valor'])}</strong>
        <span style="opacity:.7">{l['pct']}%</span>
      </div>''' for l in PRESUPUESTO['lineas'])}
    </div>
  </div>
</section>

<section class="section-alt" id="canales">
  <div class="wrap reveal">
    <p class="kicker">Divulgación</p>
    <h2>Canales CTIC</h2>
    <div class="canal-stage">
      <div class="canal-hub" id="canalHub">
        <p class="hub-label">Canal activo</p>
        <h3 id="canalTitle">{CANALES[0]}</h3>
        <p id="canalDesc">Medio de divulgación para fortalecer capacidades institucionales en CTi.</p>
      </div>
      <div class="canal-mosaic" id="canalMosaic">
        {''.join(f'''<button class="canal-tile{' on' if i==0 else ''}" type="button" data-c="{c}">
          <span class="ci">{str(i+1).zfill(2)}</span><b>{c}</b>
        </button>''' for i,c in enumerate(CANALES))}
      </div>
    </div>
  </div>
</section>

<section id="servicios">
  <div class="wrap reveal">
    <p class="kicker">Portafolio</p>
    <h2>Servicios del Observatorio CTi</h2>
    <div class="svc-mosaic" id="svcMosaic">
      {''.join(f'''<button class="svc-tile" type="button" data-i="{i}">
        <span class="sn">0{i+1}</span><b>{s["t"]}</b><span>{s["d"]}</span>
      </button>''' for i,s in enumerate(SERVICIOS))}
    </div>
    <div class="svc-detail" id="svcDetail"></div>
  </div>
</section>

<div class="marquee" aria-hidden="true"><div class="marquee-track">{''.join(f'<span>{f}</span>' for f in FUENTES+FUENTES)}</div></div>

<section id="capacidades" class="section-alt">
  <div class="wrap reveal">
    <p class="kicker">Capacidades</p>
    <h2>Perfil, herramientas y redes</h2>
    <div class="bento bento-4" style="margin:1.2rem 0">
      {''.join(f'<article class="card"><h3>{c["t"]}</h3><p>{c["d"]}</p></article>' for c in CAPACIDADES)}
    </div>
    <div class="lineas">
      {''.join(f'<article class="linea"><h3>{l["t"]}</h3><p>{l["d"]}</p></article>' for l in LINEAS)}
    </div>
  </div>
</section>

<section class="tray-section" id="estudios">
  <div class="wrap reveal">
    <p class="kicker">Trayectoria demostrada</p>
    <h2>Estudios VT/IC realizados con evidencia</h2>
    <p class="sub">Casos reales entregados desde CEITTO: reportes interactivos, tableros, anexos técnicos y dashboards en operación.</p>
    <div class="tray-stats">
      <div class="tray-stat"><b>{len(ESTUDIOS)}</b><span>Estudios priorizados</span></div>
      <div class="tray-stat"><b>{sum(len(e['evidencias']) for e in ESTUDIOS)}</b><span>Evidencias enlazadas</span></div>
      <div class="tray-stat"><b>HTML · PDF · Web</b><span>Formatos de entrega</span></div>
      <div class="tray-stat"><b>CEITTO</b><span>Capacidad instalada</span></div>
    </div>
    <div class="tray-rail" id="trayRail">
      {''.join(f'''<button class="tray-chip{' on' if i==0 else ''}" type="button" data-i="{i}">
        <span class="n">0{i+1}</span>
        <b>{e['t']}</b>
        <span>{e['d']}</span>
      </button>''' for i,e in enumerate(ESTUDIOS))}
    </div>
    <div class="tray-stage">
      <div class="tray-preview" id="trayPreview"></div>
      <aside class="tray-side" id="traySide"></aside>
    </div>
  </div>
</section>

<section id="piloto" class="section-alt">
  <div class="wrap reveal">
    <p class="kicker">Piloto</p>
    <h2>Primer caso de uso</h2>
    <div class="piloto" style="margin-top:1.2rem">
      <div class="piloto-visual"></div>
      <div class="piloto-copy">
        <h3>Indicadores de bienestar → permanencia, graduación y éxito académico</h3>
        <p>Caso demostrativo para conectar evidencia social con trayectoria estudiantil.</p>
      </div>
    </div>
  </div>
</section>

<section class="cta">
  <div class="wrap">
    <blockquote>
      La inteligencia artificial <strong>no reemplaza</strong> a las personas: las <strong>complementa</strong>.
      <cite>En el Observatorio CTi, la IA refuerza el criterio de los equipos humanos y ayuda a decidir con evidencia, de forma ética y responsable.</cite>
    </blockquote>
  </div>
</section>

<script>
const PROBLEMAS = {json.dumps(PROBLEMAS, ensure_ascii=False)};
const VENTAJAS_PDI = {json.dumps(VENTAJAS_PDI, ensure_ascii=False)};
const FLOW={json.dumps({n["id"]:n for n in FLOW},ensure_ascii=False)};
const OBJ={json.dumps(OBJ,ensure_ascii=False)};
const PLAN_DATA = {json.dumps(PLAN, ensure_ascii=False)};
const PILARES = {json.dumps(PILARES, ensure_ascii=False)};
const VENTAJAS = {json.dumps(VENTAJAS, ensure_ascii=False)};
const SERVICIOS = {json.dumps(SERVICIOS, ensure_ascii=False)};
const ESTUDIOS = {json.dumps(ESTUDIOS, ensure_ascii=False)};
document.getElementById('menu').onclick=()=>document.getElementById('links').classList.toggle('open');
document.querySelectorAll('#links a').forEach(a=>{{
  a.addEventListener('click',()=>document.getElementById('links').classList.remove('open'));
}});
window.addEventListener('resize',()=>{{
  if(innerWidth>900) document.getElementById('links').classList.remove('open');
}});

function trayPreviewHtml(e, ev){{
  if(!ev){{
    return `<div class="tray-fallback"><p class="badge">${{e.tag}}</p><h3>${{e.t}}</h3><p>${{e.blurb}}</p></div>`;
  }}
  if(ev.tipo==='html'){{
    return `<iframe title="${{ev.label}}" src="${{ev.src}}" loading="lazy"></iframe>`;
  }}
  if(ev.tipo==='pdf'){{
    return `<iframe title="${{ev.label}}" src="${{ev.src}}#view=FitH" loading="lazy"></iframe>
      <div style="position:absolute;right:12px;bottom:12px"><a href="${{ev.src}}" target="_blank" rel="noopener">Abrir PDF</a></div>`;
  }}
  // URLs externas no se embeben (bloquean iframe / sitio caído): tarjeta de acceso directo
  return `<div class="tray-fallback">
      <p class="badge">${{e.tag}} · acceso directo</p>
      <h3>${{ev.label}}</h3>
      <p>${{e.blurb}}</p>
      <p style="font-size:.85rem;opacity:.75;margin-bottom:1rem">Este recurso no se puede embeber aquí. Ábrelo en una pestaña nueva.</p>
      <a href="${{ev.src}}" target="_blank" rel="noopener">Abrir ${{ev.label}}</a>
    </div>`;
}}

function renderTray(i, evIdx=0){{
  const e = ESTUDIOS[i];
  const ev = e.evidencias[evIdx] || null;
  document.getElementById('trayPreview').innerHTML = trayPreviewHtml(e, ev);
  const list = e.evidencias.length
    ? e.evidencias.map((x,n)=>`<button type="button" class="${{n===evIdx?'on':''}}" data-e="${{n}}"><span>${{x.label}}</span><span class="kind">${{x.tipo}}</span></button>`).join('')
    : `<p style="color:rgba(255,255,255,.65);font-size:.9rem;margin:0">Evidencia documental de cierres de proyectos VT/IC.</p>`;
  document.getElementById('traySide').innerHTML = `
    <p class="tag">${{e.tag}}</p>
    <h3>${{e.t}}</h3>
    <div class="metric-row"><b>${{e.metric}}</b><span>${{e.metric_l}}</span></div>
    <p>${{e.blurb}}</p>
    <div class="tray-ev">${{list}}</div>
    ${{ev ? `<a class="cta-ev" href="${{ev.src}}" target="_blank" rel="noopener">Abrir evidencia completa</a>` : ''}}`;
  document.querySelectorAll('#traySide .tray-ev button').forEach(btn=>{{
    btn.onclick=()=>renderTray(i, +btn.dataset.e);
  }});
}}
document.querySelectorAll('#trayRail .tray-chip').forEach(btn=>{{
  btn.onclick=()=>{{
    document.querySelectorAll('#trayRail .tray-chip').forEach(b=>b.classList.remove('on'));
    btn.classList.add('on');
    renderTray(+btn.dataset.i, 0);
  }};
}});
if(document.getElementById('trayRail')) renderTray(0,0);

function renderProb(i){{
  const p = PROBLEMAS[i];
  const panel = document.getElementById('probPanel');
  if(!panel) return;
  panel.className = 'prob-panel' + (p.tipo==='solucion' ? ' solucion' : '');
  panel.innerHTML = `<p class="tag">Contexto Colmayor</p><h3>${{p.titulo}}</h3><p>${{p.desc}}</p><div class="efecto"><strong>Implicación:</strong> ${{p.efecto}}</div>`;
}}
document.querySelectorAll('#probList .prob-btn').forEach(btn=>{{
  btn.onclick=()=>{{
    document.querySelectorAll('#probList .prob-btn').forEach(b=>b.classList.remove('on'));
    btn.classList.add('on');
    renderProb(+btn.dataset.i);
  }};
}});

function renderPdi(i){{
  const v = VENTAJAS_PDI[i];
  const panel = document.getElementById('pdiPanel');
  if(!panel) return;
  panel.innerHTML = `
    <h3>${{v.nombre}}</h3>
    <p class="foco">${{v.foco}}</p>
    <ul class="pdi-inds">${{v.indicadores.map((ind,n)=>`<li style="animation-delay:${{n*0.05}}s"><b>${{ind.t}}</b><span>${{ind.m}}</span></li>`).join('')}}</ul>`;
}}
document.querySelectorAll('#pdiTabs .pdi-tab').forEach(btn=>{{
  btn.onclick=()=>{{
    document.querySelectorAll('#pdiTabs .pdi-tab').forEach(b=>b.classList.remove('on'));
    btn.classList.add('on');
    renderPdi(+btn.dataset.i);
  }};
}});


function renderFlow(id){{
  const d=FLOW[id];
  document.getElementById('flowDetail').innerHTML=`
    <div class="flow-step">${{d.n}}</div>
    <div>
      <h3>${{d.titulo}} · ${{d.fase}}</h3>
      <p class="proceso">${{d.proceso}}</p>
      <div class="flow-grid">
        <div class="flow-box"><h4>Actividades</h4><ul>${{d.actividades.map(a=>`<li>${{a}}</li>`).join('')}}</ul></div>
        <div class="flow-box"><h4>Entradas / salidas</h4><p><strong>En:</strong> ${{d.entradas}}<br/><strong>Out:</strong> ${{d.salidas}}</p></div>
        <div class="flow-box"><h4>Responsable</h4><p>${{d.responsable}}</p></div>
      </div>
    </div>`;
}}
document.querySelectorAll('.nodo').forEach(n=>{{
  n.onclick=()=>{{document.querySelectorAll('.nodo').forEach(x=>x.classList.remove('activo'));n.classList.add('activo');renderFlow(n.dataset.id);}};
}});
document.querySelector('.nodo')?.classList.add('activo');

document.querySelectorAll('.obj-card').forEach(btn=>{{
  btn.onclick=()=>{{
    document.querySelectorAll('.obj-card').forEach(b=>b.classList.remove('on'));
    btn.classList.add('on');
    const o=OBJ[+btn.dataset.i];
    document.getElementById('objPanel').innerHTML=`<strong>${{o.t}}</strong><p>${{o.d}}</p>`;
  }};
}});

document.querySelectorAll('#kpiTabs .kpi-tab').forEach(tab=>{{
  tab.onclick=()=>{{
    document.querySelectorAll('#kpiTabs .kpi-tab').forEach(t=>t.classList.remove('on'));
    tab.classList.add('on');
    const dim=tab.dataset.dim;
    document.querySelectorAll('#kpiGrid .kpi').forEach(k=>{{
      k.style.display=(dim==='all'||k.dataset.dim===dim)?'':'none';
    }});
  }};
}});

/* Valor pillars */
document.querySelectorAll('#pillarStack .pillar-btn').forEach(btn=>{{
  btn.onclick=()=>{{
    document.querySelectorAll('#pillarStack .pillar-btn').forEach(b=>b.classList.remove('on'));
    btn.classList.add('on');
    const p=PILARES[+btn.dataset.i];
    document.getElementById('valorPanel').innerHTML=`<p class="eyebrow">Pilar activo</p><h3>${{p.t}}</h3><p>${{p.d}}</p>`;
  }};
}});

/* Ventajas chips */
document.querySelectorAll('#advRail .adv-chip').forEach(btn=>{{
  btn.onclick=()=>{{
    document.querySelectorAll('#advRail .adv-chip').forEach(b=>b.classList.remove('on'));
    btn.classList.add('on');
    const v=VENTAJAS[+btn.dataset.i];
    const spot=document.getElementById('advSpot');
    spot.classList.add('show');
    spot.innerHTML=`<strong>${{v.t}}</strong>: ${{v.d}}`;
  }};
}});

/* Roadmap / Plan */
function renderRoad(i){{
  const p=PLAN_DATA[i];
  document.querySelectorAll('#roadTrack .road-step').forEach((b,idx)=>b.classList.toggle('on',idx===i));
  document.getElementById('roadPanel').innerHTML=`
    <div class="road-badge">${{p.fase}}</div>
    <div>
      <h3>${{p.t}}</h3>
      <ul class="road-items">${{p.items.map((it,j)=>`<li style="animation-delay:${{j*0.05}}s">${{it}}</li>`).join('')}}</ul>
    </div>`;
}}
document.querySelectorAll('#roadTrack .road-step').forEach(btn=>{{
  btn.onclick=()=>renderRoad(+btn.dataset.i);
}});

/* Canales mosaic */
document.querySelectorAll('#canalMosaic .canal-tile').forEach(btn=>{{
  btn.onclick=()=>{{
    document.querySelectorAll('#canalMosaic .canal-tile').forEach(b=>b.classList.remove('on'));
    btn.classList.add('on');
    document.getElementById('canalTitle').textContent=btn.dataset.c;
    document.getElementById('canalDesc').textContent='Medio de divulgación para fortalecer capacidades institucionales en CTi.';
  }};
}});

/* Servicios mosaic */
document.querySelectorAll('#svcMosaic .svc-tile').forEach(btn=>{{
  btn.onclick=()=>{{
    document.querySelectorAll('#svcMosaic .svc-tile').forEach(b=>b.classList.remove('on'));
    btn.classList.add('on');
    const s=SERVICIOS[+btn.dataset.i];
    const d=document.getElementById('svcDetail');
    d.classList.add('show');
    d.innerHTML=`<strong>${{s.t}}</strong>: ${{s.d}}`;
  }};
}});

const io=new IntersectionObserver(es=>es.forEach(e=>{{if(e.isIntersecting)e.target.classList.add('on');}}),{{threshold:.1}});
document.querySelectorAll('.reveal').forEach(el=>io.observe(el));
const secs=[...document.querySelectorAll('section[id],header[id]')];
const links=[...document.querySelectorAll('.nav-links a')];
window.addEventListener('scroll',()=>{{
  const max=document.documentElement.scrollHeight-innerHeight;
  document.getElementById('bar').style.width=`${{(scrollY/max)*100}}%`;
  let cur=secs[0]?.id;
  secs.forEach(s=>{{if(scrollY>=s.offsetTop-110)cur=s.id;}});
  links.forEach(a=>a.classList.toggle('on',a.getAttribute('href')===`#${{cur}}`));
}});
</script>
</body>
</html>
'''

(OUT / "index.html").write_text(html, encoding="utf-8")
assert "Seleccione un objetivo" not in html
assert "no reemplaza" in html
assert "RTX 5090" in html
assert "Eaton DX2000LAN" in html
assert "Implementación de IA" in html
assert "Red y conectividad" not in html
assert "Dell Precision" not in html
assert "KPI-01" in html
assert 'id="problema"' in html
assert 'id="ventajas-pdi"' in html
assert "Academia transformadora" in html
assert 'id="estudios"' in html
assert "evidencias/camara" in html
assert "mgdalena-medio.vercel.app" in html
assert "convocaradar-web.vercel.app" in html
assert "\u2014" not in html
assert OBJETIVO_CLARO.split()[0] in html
print("OK", OUT / "index.html", "total", PRESUPUESTO["total"])

