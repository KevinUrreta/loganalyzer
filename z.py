
class notificacion:
    """
    
    """
    def __init__(self) -> None:
        """
        
        """
        self.estado :list[str] = []
        print(self.estado)

app = notificacion()
app.estado.append("Hola buenas tardes")
print(app.estado)
for item in app.estado:
    app.estado.append(item)
print(app.estado)