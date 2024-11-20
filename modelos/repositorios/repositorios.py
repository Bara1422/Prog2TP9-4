from modelos.repositorios.repositorio_polizas import RepositorioPoliza

repo_polizas = None

def obtenerRepoPolizas()->RepositorioPoliza:
    global repo_polizas
    if not isinstance(repo_polizas,RepositorioPoliza):
        repo_polizas = RepositorioPoliza()
    return repo_polizas