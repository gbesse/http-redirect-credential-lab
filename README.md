# http-redirect-credential-lab

## Français

Tester les secrets transmis lors de redirections locales.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m http_redirect_credential_lab examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Deux vrais serveurs localhost sur des ports distincts : compare redirection urllib standard et retrait des en-têtes sensibles lorsque l’origine change. Canaris fictifs uniquement.

### Limites

Banc HTTP local, pas audit de tous les clients ni TLS. Le comportement standard est observé sur la version Python exécutée ; aucun secret ni URL distante accepté.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Test secrets forwarded during local redirects.

Synthetic data; no network access or secret required.

```sh
python -m http_redirect_credential_lab examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Two actual localhost servers on distinct ports compare standard urllib redirection with sensitive-header removal on origin changes. Synthetic canaries only.

### Limits

Local HTTP harness, not an audit of every client or TLS. Standard behavior is observed on the running Python version; no secrets or remote URLs accepted.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Probar secretos transmitidos en redirecciones locales.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m http_redirect_credential_lab examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Dos servidores localhost reales en puertos distintos comparan redirección urllib estándar y retirada de cabeceras sensibles al cambiar origen. Solo canarios ficticios.

### Límites

Banco HTTP local, no auditoría de todos los clientes ni TLS. Comportamiento estándar observado en Python ejecutado; sin secretos ni URL remotas.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://www.rfc-editor.org/rfc/rfc9110.html#section-15.4
