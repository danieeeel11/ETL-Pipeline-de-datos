
def descargahtml():
    urls = {
        "eltiempo": "https://www.eltiempo.com/",
        "publimetro": "https://www.publimetro.co/"
    }
    # Configurar cliente de S3
    s3_client = boto3.client("s3")
    # Obtener fecha actual
    current_date = datetime.now().strftime("%Y-%m-%d")
    contentHtml = ""
    for newspaper, url in urls.items():
        response = urllib.request.urlopen(url)
        content = response.read()
        contentHtml = content
        # Definir la ruta en S3
        s3_path = f"news/raw/{newspaper}-{current_date}.html"
        # Subir contenido a S3
        s3_client.put_object(Bucket="parcial1bucket1",
                             Key=s3_path,
                             Body=content)
        print(f"Contenido de {newspaper} guardado en S3: {s3_path}")
    return content


descargahtml()
