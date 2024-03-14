from sqlalchemy import create_engine, ForeignKey, func, Column, update, desc, insert
from sqlalchemy import String, VARCHAR, CHAR, Boolean, BINARY, Integer, Numeric, DECIMAL, DATETIME, TIME, Date
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from icecream import ic


Base=declarative_base()

class Usuarios(Base):
    __tablename__="Usuarios"
    idUsuario = Column("idUsuario", Integer, primary_key = True)
    NombreUsuario = Column("NombreUsuario", VARCHAR(50), nullable = False)
    Contrasena = Column("Contrasena", VARCHAR(20), nullable = False)
    Status = Column("Status", Boolean, default = False)
    Activo = Column("Activo", Boolean, default = True)
    
    def __init__(self, NombreUsuario, Contrasena, Status = False, Activo = True):
        self.NombreUsuario = NombreUsuario
        self.Contrasena = Contrasena
        self.Status = Status
        self.Activo = Activo
    
    def __repr__(self):
        return f"{self.idUsuario}, {self.NombreUsuario}, {self.Contrasena}, {self.status}, {self.Activo}"
    
class Cliente(Base):
    __tablename__="Cliente"
    idCliente = Column("idCliente", Integer, primary_key = True)
    NombreCliente = Column("NombreCliente", VARCHAR(50), nullable = False)
    Correo = Column("Correo", VARCHAR(50), nullable = False)
    Telefono = Column("Telefono", VARCHAR(10), nullable = False)
    Status = Column("Status", Boolean, default = False)
    Activo = Column("Activo", Boolean, default = True)
    idUsuario = Column("idUsuario", Integer, ForeignKey("Usuario.idUsuario"))
    
    def __init__(self, NombreCliente, Correo, Telefono, idUsuario, Status = False, Activo = True):
        self.NombreCliente = NombreCliente
        self.Correo = Correo
        self.Telefono = Telefono
        self.Status = Status
        self.Activo = Activo
        self.idUsuario = idUsuario
    
    def __repr__(self):
        return f"{self.idCliente}, {self.NombreCliente}, {self.Correo}, {self.Telefono}, {self.Activo}, {self.idUsuario}"
   
class Rancho(Base):
    __tablename__ = "Rancho"
    idRancho = Column("idRancho", Integer, primary_key = True)
    NombreRancho = Column("NombreRancho", VARCHAR(50), nullable = False)
    Pais = Column("Pais", VARCHAR(30), nullable = False)
    Estado = Column("Estado", VARCHAR(40), nullable = False)
    Localidad = Column("Localidad", VARCHAR(50), nullable = False)
    Direccion = Column("Direccion", VARCHAR(50), nullable = False)
    CoordenadasRancho = Column("CoordenadasRancho", String)
    Status = Column("Status", Boolean, default = False)
    Activo = Column("Activo", Boolean, default = True)
    idCliente = Column("idCliente", Integer, ForeignKey("Cliente.idCliente"))
    
    def __init__(self, NombreRancho, Pais, Estado, Localidad, Direccion, CoordenadasRancho, idCliente, Status = False, Activo = True):
        self.NombreRancho = NombreRancho
        self.Pais = Pais
        self.Estado = Estado
        self.Localidad = Localidad
        self.Direccion = Direccion
        self.CoordenadasRancho = CoordenadasRancho
        self.Status = Status
        self.Activo = Activo
        self.idCliente = idCliente
        
    def __repr__(self):
        return f"{self.idRancho}, {self.NombreRancho}, {self.Pais}, {self.Estado}, {self.Localidad}, {self.Direccion}, {self.Activo}, {self.CoordenadasRancho} ,{self.idCliente}"

class Maquina(Base):
    __tablename__ = "Maquina"
    idMaquina = Column("idMaquina",Integer,primary_key=True)
    versionMaquina = Column("versionMaquina", VARCHAR(15), nullable = False)
    FechaCreacion = Column("FechaCreacion", DATETIME, nullable = False)
    HorasTrabajadas = Column("HorasTrabajadas", Numeric(10, 2))
    Status = Column("Status", Boolean, default = False)
    Activo = Column("Activo", Boolean, default = True)
    idRancho = Column("idRancho", Integer, ForeignKey("Rancho.idRancho"))
    
    def __init__(self, versionMaquina, FechaCreacion, HorasTrabajadas, idRancho, Status = False, Activo = True):
        self.versionMaquina = versionMaquina
        self.FechaCreacion = FechaCreacion
        self.HorasTrabajadas = HorasTrabajadas
        self.Status = Status
        self.Activo = Activo
        self.idRancho = idRancho
    
    def __repr__(self):
        return f"{self.idMaquina}, {self.versionMaquina}, {self.FechaCreacion}, {self.HorasTrabajadas}, {self.Activo}, {self.idRancho}"

class Caracteristicas(Base):
    __tablename__="Caracteristicas"
    idCaracteristicas = Column("idCaracteristicas", Integer, primary_key = True)
    VelMaxFuncionamiento = Column("VelocidadMaximaDeFuncionamiento", DECIMAL(5, 2))
    Consumo = Column("VoltajeConsumidoHora", Numeric(9, 2), nullable = False)
    Iluminacion = Column("Iluminacion", Integer, nullable = False)
    Peso = Column("Peso", Numeric(10, 3), nullable = False)
    Status = Column("Status", Boolean, default = False)
    Activo = Column("Activo", Boolean, default = True)
    idMaquina = Column("idMaquina", Integer, ForeignKey("Maquina.idMaquina"))
    
    def __init__(self, VelMaxFuncionamiento, Consumo, Iluminacion, Peso, idMaquina, Status = False, Activo = True):
        self.VelMaxFuncionamiento = VelMaxFuncionamiento
        self.Consumo = Consumo
        self.Iluminacion = Iluminacion
        self.Peso = Peso
        self.Status = Status
        self.Activo = Activo
        self.idMaquina = idMaquina
    
    def __repr__(self):
        return f"{self.idCaracteristicas}, {self.VelMaxFuncionamiento}, {self.Consumo}, {self.Iluminacion}, {self.Peso}, {self.Activo}, {self.idMaquina}"
 
class Actividad(Base):
    __tablename__="Actividad"
    idActividad = Column("idActividad", Integer, primary_key = True)
    FechaActividad = Column("FechaActividad", DATETIME)
    HoraInicio = Column("HoraInicio", TIME)
    HoraFinalizada = Column("HoraFinalizada", TIME)
    DistanciaRecorrida = Column("DistanciaRecorrida", Numeric(10, 3), nullable = False)
    Status = Column("Status", Boolean, default = False)
    Activo = Column("Activo", Boolean, default = True)
    idMaquina = Column("idMaquina", Integer, ForeignKey("Maquina.idMaquina"))
    
    def __init__(self, FechaActividad, HoraInicio, HoraFinalizada, DistanciaRecorrida, idMaquina, Status = False, Activo = True):
        self.FechaActividad = FechaActividad
        self.HoraInicio = HoraInicio
        self.HoraFinalizada = HoraFinalizada
        self.DistanciaRecorrida = DistanciaRecorrida
        self.Status = Status
        self.Activo = Activo
        self.idMaquina = idMaquina
    
    def __repr__(self):
        return f"{self.idActividad}, {self.FechaActividad}, {self.HoraInicio}, {self.HoraFinalizada}, {self.DistanciaRecorrida}, {self.Activo}, {self.idMaquina}"

class Departamento(Base):
    __tablename__ = "Departamento"
    idDepartamento = Column("idDepartamento", Integer, primary_key = True)
    NombreDepartamento = Column("NombreDepartamento", VARCHAR(30), nullable = False)
    PersonaEncargada = Column("PersonaEncargada", VARCHAR(40), nullable = False)
    Status = Column("Status", Boolean, default = False)
    Activo = Column("Activo", Boolean, default = True)
    
    def __init__(self, NombreDepartamento, PersonaEncargada, Status = False, Activo = True):
        self.NombreDepartamento = NombreDepartamento
        self.PersonaEncargada = PersonaEncargada
        self.Status = Status
        self.Activo = Activo
    
    def __repr__(self):
        return f"{self.idDepartamento}, {self.NombreDepartamento}, {self.PersonaEncargada}, {self.Activo}"

class Elemento(Base):
    __tablename__ = "Elemento"
    idElemento = Column("idElemento", Integer, primary_key = True)
    NombreElemento = Column("NombreElemento", VARCHAR(30), nullable = False)
    Caracteristicas = Column("Caracteristicas", String, nullable = False)
    Proveedor = Column("Proveedor", VARCHAR(30), nullable = False)
    Status = Column("Status", Boolean, default = False)
    Activo = Column("Activo", Boolean, default = True)
    idDepartamento = Column("idDepartamento", Integer, ForeignKey("Departamento.idDepartamento"))
    
    def __init__(self, NombreElemento, Caracteristicas, Proveedor, idDepatamento, Status = False, Activo = True):
        self.NombreElemento = NombreElemento
        self.Caracteristicas = Caracteristicas
        self.Proveedor = Proveedor
        self.Status = Status
        self.Activo = Activo
        self.idDepatamento = idDepatamento
    
    def __repr__(self):
        return f"{self.idElemento}, {self.NombreElemento}, {self.Caracteristicas}, {self.Proveedor}, {self.Activo}, {self.idDepatamento}"

class Mantenimiento(Base):
    __tablename__ = "Mantenimiento"
    idMantenimiento = Column("idMantenimiento", Integer, primary_key = True)
    FechaMantenimiento = Column("FechaMantenimiento", DATETIME)
    ElementosChecado = Column("ElementosChecado", VARCHAR(100))
    Nota = Column("Nota", String)
    Status = Column("Status", Boolean, default = False)
    Activo = Column("Activo", Boolean, default = True)
    idMaquina = Column("idMaquina", Integer, ForeignKey("Maquina.idMaquina"))
    idElemento = Column("idElemento", Integer, ForeignKey("Elemento.idElemento"))
    
    def __init__(self, FechaMantenimiento, ElementosChecado, Nota, idMaquina, idElemento, Status = False, Activo = True):
        self.FechaMantenimiento = FechaMantenimiento
        self.ElementosChecado = ElementosChecado
        self.Nota = Nota
        self.Status = Status
        self.Activo = Activo
        self.idMaquina = idMaquina
        self.idElemento = idElemento
    
    def __repr__(self):
        return f"{self.idMantenimiento}, {self.FechaMantenimiento}, {self.ElementosChecado}, {self.Activo}, {self.Nota}, {self.idMaquina}, {self.idElemento}"

# =============================================================================
# class Elemento_Maquina(Base):
#     __tablename__ = "Elemento_Maquina"
#     idMaquina = Column("idMaquina", Integer, ForeignKey("Maquina.idMaquina"))
#     idElemento = Column("idElemento", Integer, ForeignKey("Elemento.idElemento"))
#     
#     def __init__(self, idMaquina, idElemento):
#         self.idMaquina = idMaquina
#         self.idElemento = idElemento
# 
#     def __repr__(self):
#         return f"{self.idMantenimiento}, {self.FechaMantenimiento}"
# =============================================================================

class Variedad(Base):
    __tablename__= "Variedad"
    idVariedad = Column("idVariedad", Integer, primary_key=True)
    Nombre = Column("Nombre", VARCHAR(30), nullable = False)
    TiempoMaduracion = Column("TiempoMaduracion", VARCHAR(7))
    TamanoPromedio = Column("TamanoPromedio", Numeric(5,2))
    CostoPorHectareaPlantada = Column("CostoPorHectareaPlantada", Integer)
    Status = Column("Status", Boolean, default = False)
    Activo = Column("Activo", Boolean, default = True)
    
    def __init__(self, Nombre, TiempoMaduracion, TamanoPromedio, CostoPorHectareaPlantada, Status = False, Activo = True):
        self.Nombre = Nombre
        self.TiempoMaduracion = TiempoMaduracion
        self.TamanoPromedio = TamanoPromedio
        self.CostoPorHectareaPlantada = CostoPorHectareaPlantada
        self.Status = Status
        self.Activo = Activo
        
    def __repr__(self):
        return "{self.idVariedad}, {self.Nombre}, {self.TiempoMaduracion}, {self.CostoPorHectareaPlantada}, {self.Activo}"
    
class Parcela(Base):
    __tablename__="Parcela"
    idParcela = Column("idParcela",Integer, primary_key=True)
    NombreParcela = Column("nombreParcela", VARCHAR(40), nullable = False)
    TamanoHectarea = Column("TamanoHectarea", Numeric(10,4), nullable = False)
    FechaPlantacion = Column("FechaPlantacion", Date, nullable = False)
    CantidadPlantada = Column("CantidadPlantada", Integer, nullable = False)
    SeparacionEntreCultivo = Column("SeparacionEntreCultivo", DECIMAL(6,2), nullable = False)
    DistanciaEntreSurcos = Column("DistanciaEntreSurcos", DECIMAL(6,2), nullable = False)
    CoordenadasParcela = Column("CoordenadasParcela", String, nullable = False)
    EstadoParcela = Column("EstadoParcela", VARCHAR(40))
    Status = Column("Status", Boolean, default = False)
    Activo = Column("Activo", Boolean, default = True)
    idRancho = Column("idRancho", Integer, ForeignKey("Rancho.idRancho"))
    idVariedad = Column("idVariedad", Integer, ForeignKey("Variedad.idVariedad"))
    
    def __init__(self, NombreParcela, TamanoHectarea,FechaPlantacion, CantidadPlantada, SeparacionEntreCultivo, DistanciaEntreSurcos, CoordenadasParcela, EstadoParcela, idRancho, idVariedad, Status = False, Activo = True):
        self.NombreParcela = NombreParcela
        self.TamanoHectarea = TamanoHectarea
        self.FechaPlantacion = FechaPlantacion
        self.CantidadPlantada = CantidadPlantada
        self.SeparacionEntreCultivo = SeparacionEntreCultivo
        self.DistanciaEntreSurcos = DistanciaEntreSurcos
        self.CoordenadasParcela = CoordenadasParcela
        self.EstadoParcela = EstadoParcela
        self.Status = Status
        self.Activo = Activo
        self.idRancho = idRancho
        self.idVariedad = idVariedad
        
    def __repr__(self):
        return f"{self.idParcela}, {self.NombreParcela}, {self.TamanoHectarea}, {self.FechaPlantacion}, {self.CantidadPlantada}, {self.SeparacionEntreCultivo}, {self.DistanciaEntreSurcos}, {self.CoordenadasParcela}, {self.EstadoParcela}, {self.Activo}, {self.idRancho}, {self.idVariedad}"

class Cosecha(Base):
    __tablename__ = "Cosecha"
    idCosecha = Column("idCosecha", Integer, primary_key = True)
    InicioCosecha = Column("InicioCosecha", Date)
    FinCosecha = Column("FinCosecha", Date)
    CantidadContadaDeLaCosecha = Column("CantidadContadaDeLaCosecha", Integer)
    HorasDeOperacion = Column("HorasDeOperacion", Numeric(5, 2))
    PesoEstimadoCosecha = Column("PesoEstimadoCosecha", Numeric(10, 2))
    Nota = Column("Nota", String)
    Status = Column("Status", Boolean, default = False)
    Activo = Column("Activo", Boolean, default = True)
    idRancho = Column("idRancho", Integer, ForeignKey("Rancho.idRancho"))
    idParcela = Column("idParcela", Integer, ForeignKey("Parcela.idParcela"))
    idMaquina = Column("idMaquina", Integer, ForeignKey("Maquina.idMaquina"))
    
    def __init__(self, idRancho, idParcela, idMaquina, InicioCosecha = None, FinCosecha = None, CantidadContadaDeLaCosecha = 0, HorasDeOperacion = None, PesoEstimadoCosecha = 0, Nota = None, Status = False, Activo = True):
        self.InicioCosecha = InicioCosecha
        self.FinCosecha = FinCosecha
        self.CantidadContadaDeLaCosecha = CantidadContadaDeLaCosecha
        self.HorasDeOperacion = HorasDeOperacion
        self.PesoEstimadoCosecha = PesoEstimadoCosecha
        self.Nota = Nota
        self.Status = Status
        self.Activo = Activo
        self.idMaquina = idMaquina
        self.idRancho = idRancho
        self.idParcela = idParcela
        
    def __repr__(self):
        return f"{self.idCosecha}, {self.InicioCosecha}, {self.FinCosecha}, {self.CantidadContadaDeLaCosecha}, {self.HorasDeOperacion}, {self.PesoEstimadoCosecha}, {self.Nota}, {self.Activo}, {self.idMaquina}, {self.idRancho}, {self.idParcela}"
    
class Estandares(Base):
    __tablename__ = "Estandares"
    idEstandares = Column("idEstandares", Integer, primary_key = True)
    Calibre = Column("Calibre", VARCHAR(20), nullable = False)
    TamanoMaximo = Column("TamanoMaximo", Integer, nullable = False)
    TamanoMinimo = Column("TamanoMinimo", Integer, nullable = False)
    PesoMaximo = Column("PesoMaximo", Numeric(5, 2))
    PesoMinimo = Column("PesoMinimo", Numeric(5, 2))
    Area = Column("Area", Numeric(6, 2))
    Status = Column("Status", Boolean, default = False)
    Activo = Column("Activo", Boolean, default = True)
    
    def __init__(self, Calibre, TamanoMaximo, TamanoMinimo, PesoMaximo, PesoMinimo, Area, Status = False, Activo = True):
        self.Calibre = Calibre
        self.TamanoMaximo = TamanoMaximo
        self.TamanoMinimo = TamanoMinimo
        self.PesoMaximo = PesoMaximo
        self.PesoMinimo = PesoMinimo
        self.Area = Area
        self.Status = Status
        self.Activo = Activo
        
    def __repr__(self):
        return f"{self.idEstandares}, {self.Calibre}, {self.TamanoMaximo}, {self.TamanoMinimo}, {self.PesoMaximo}, {self.PesoMinimo}, {self.Area},{self.Activo}"
    
class Pasada(Base):
    __tablename__ = "Pasada"
    idPasada = Column("idPasada", Integer, primary_key = True, autoincrement=True)
    InicioPasada = Column("InicioPasada", Date)
    FinPasada = Column("FinPasada", Date, nullable = True)
    CantidadObservada = Column("CantidadObservada", Integer, nullable = False, default = 0)
    Suprema = Column("Suprema", Integer, default = 0)
    Primera = Column("Primera", Integer, default = 0)
    Segunda = Column("Segunda", Integer, default = 0)
    Tercera = Column("Tercera", Integer, default = 0)
    Cuarta = Column("Cuarta", Integer, default = 0)
    PesoTotal = Column("PesoTotal", DECIMAL(15,3), default = 0)
    Status = Column("Status", Boolean, default = False)
    Activo = Column("Activo", Boolean, default = True)
    idCosecha = Column("idCosecha", Integer, ForeignKey("Cosecha.idCosecha"))
    
    def __init__(self,idCosecha, InicioPasada, FinPasada = None, CantidadObservada = 0, Suprema = 0, Primera = 0, Segunda = 0, Tercera = 0, Cuarta = 0, PesoTotal = 0, Status = False, Activo = True):
        self.InicioPasada = InicioPasada
        self.FinPasada = FinPasada
        self.CantidadObservada = CantidadObservada
        self.Suprema = Suprema
        self.Primera = Primera
        self.Segunda = Segunda
        self.Tercera = Tercera
        self.Cuarta = Cuarta
        self.PesoTotal = PesoTotal
        self.Status = Status
        self.Activo = Activo
        self.idCosecha = idCosecha
        
    def __repr__(self):
        return f"({self.idPasada}) {self.InicioPasada} {self.FinPasada} {self.CantidadObservada} {self.Suprema} {self.Primera} {self.Segunda} {self.Tercera} {self.Cuarta} {self.PesoTotal} {self.Activo} {self.idCosecha}"

class Rendimiento(Base):
    __tablename__ = "Rendimiento"
    idRendimiento = Column("idRendimiento", Integer, primary_key = True, autoincrement=True)
    LatitudInicial = Column("LatitudInicial", DECIMAL(10,5), nullable = True)
    LongitudInicial = Column("LongitudInicial", DECIMAL(10,5), nullable = True)
    LatitudFinal = Column("LatitudFinal", DECIMAL(10,5), nullable = True)
    LongitudFinal = Column("LongitudFinal", DECIMAL(10,5), nullable = True)
    Total = Column("Total", Integer, nullable = False, default = 0)
    Suprema = Column("Suprema", Integer, default = 0)
    Primera = Column("Primera", Integer, default = 0)
    Segunda = Column("Segunda", Integer, default = 0)
    Tercera = Column("Tercera", Integer, default = 0)
    Cuarta = Column("Cuarta", Integer, default = 0)
    Peso = Column("Peso", DECIMAL(14,3), nullable = True)
    Status = Column("Status", Boolean, default = False)
    Activo = Column("Activo", Boolean, default = True)
    idPasada = Column("idPasada", Integer, ForeignKey("Pasada.idPasada"))
    
    def __init__(self, idPasada, Latitud = None, Longitud = None, Total = 0, Suprema = 0, Primera = 0, Segunda = 0, Tercera = 0, Cuarta = 0, Peso = 0, Status = False, Activo = True):
        self.Latitud = Latitud
        self.Longitud = Longitud
        self.Total = Total
        self.Suprema = Suprema
        self.Primera = Primera
        self.Segunda = Segunda
        self.Tercera = Tercera
        self.Cuarta = Cuarta
        self.Peso = Peso
        self.Status = Status
        self.Activo = Activo
        self.idPasada = idPasada
        
    def __repr__(self):
        return f"({self.idRendimiento}) {self.Latitud} {self.Longitud} {self.Total} {self.Suprema} {self.Primera} {self.Segunda} {self.Tercera} {self.Cuarta} {self.Peso} {self.Activo} {self.idPasada}"

class DefaultData(Base):
    __tablename__ = "DefaultData"
    idDefault = Column("idDefault", Integer, primary_key = True, autoincrement = True)
    Status = Column("Status", Boolean, default = False)
    Activo = Column("Activo", Boolean, default = True)
    idCliente = Column("idCliente", Integer, ForeignKey("Cliente.idCliente"))
    idRancho = Column("idRancho", Integer, ForeignKey("Rancho.idRancho"))
    Rancho = Column("Rancho", VARCHAR(50), nullable = False)
    idVariedad = Column("idVariedad", Integer, ForeignKey("Variedad.idVariedad"))
    Variedad = Column("variedad", VARCHAR(30), nullable = False)
    idParcela = Column("idParcela", Integer, ForeignKey("Parcela.idParcela"))
    Parcela = Column("Parcela", VARCHAR(40), nullable = False)
    idCosecha = Column("idCosecha", Integer, ForeignKey("Cosecha.idCosecha"))
    
    def __init__(self, idCliente, idRancho, Rancho, idVariedad, Variedad, idParcela, Parcela, idCosecha, Status = False, Activo = True):
        self.Status = Status
        self.Activo = Activo
        self.idCliente = idCliente
        self.idRancho = idRancho
        self.Rancho = Rancho
        self.idVariedad = idVariedad
        self.Variedad = Variedad
        self.idParcela = idParcela
        self.Parcela = Parcela
        self.idCosecha = idCosecha
        
    def __repr__(self):
        return f"({self.idDefault}) {self.idCliente} {self.idRancho} {self.idVariedad} {self.idParcela} {self.idCosecha} {self.Status} {self.Activo}"

class Creacion:
    def __init__(self, Datos):
        self.Datos=Datos
        engine = create_engine(f'mssql+pyodbc://{self.Datos["User"]}:{self.Datos["Pwd"]}@{self.Datos["nameServer"]}/{self.Datos["nameDB"]}?driver=ODBC+Driver+17+for+SQL+Server')
        Base.metadata.create_all(bind = engine)
        Session = sessionmaker(bind = engine)
        self.session = Session()
    
    def cerrar(self):
        self.session.close()
    
# =============================================================================
#     def consultaidPruebaPapas(self):
#         try: 
#             idPruebaPapas = self.session.query(func.max(PruebaPapas.idPruebaPapas)).scalar()
#             return idPruebaPapas
#         except Exception as e:
#             print("Error -> Consulta: ", e)
# =============================================================================
    
    def Incremento(self, Elemento, idE, valor = 1):
        try:
            R = self.session.query(getattr(Pasada, Elemento)).filter(Pasada.idPasada == idE).scalar()
            
            if R !=None:
                rel = update(Pasada).where(Pasada.idPasada == idE).values({Elemento: R + valor})
                self.session.execute(rel)
                self.session.commit()
                #  R=self.session.query(getattr(Prueba,Elemento)).filter(Prueba.idObservacion==idE).scalar()
                #  print(R)
                return True
            else:
                ic("nones")
                return False
        except Exception as e:
            print("Error -> Incremento: ", e)
            return False
    
    
    def ConsultaLogin(self, user, password):
        user = self.session.query(Usuarios.NombreUsuario, Usuarios.idUsuario).filter_by(NombreUsuario = user, Contrasena = password).first()
        return user
    
    def ConsultaCliente(self, idUser):
        ic(idUser)
        client = self.session.query(Cliente.NombreCliente, Cliente.idCliente).filter_by(idUsuario = idUser).first()
        return client

    def ConsultaRancho(self, idCliente):
        ic(idCliente)
        ranchos = (
            self.session.query(Rancho.idRancho, Rancho.NombreRancho, Rancho.Localidad)
            .filter_by(idCliente = idCliente)
            .all()
            )
        return ranchos
    
    def ConsultaVariedad(self):
        variedades = (self.session.query(Variedad.idVariedad, Variedad.Nombre)).all()
        return variedades

    def ConsultaParcela(self, idRancho, idVariedad):
        parcelas = (
            self.session.query(Parcela.idParcela, Parcela.NombreParcela)
            .filter_by(idRancho = idRancho, idVariedad = idVariedad)
            .all()
        )
        return parcelas

    def ConsultaCosecha(self, idRancho, idParcela, idMaquina):
        cosechas = (
            self.session.query(Cosecha.idCosecha)
            .filter(Cosecha.idRancho == idRancho, Cosecha.idParcela == idParcela, Cosecha.idMaquina == idMaquina)
            .all()
        )
        return cosechas
    
    def ConsultaPasada(self, idCosecha):
        pasada = (
            self.session.query(Pasada)
            .filter(Pasada.idCosecha == idCosecha)
            .all()
        )
        return pasada

    def ConsultaDatosPasada(self, idPasada):
        self.session.commit()
        datos = (
            self.session.query(Pasada)
            .filter(Pasada.idPasada == idPasada)
            .first()
        )
        return datos
    
    def ConsultaRendimiento(self, idPasada):
        rendimiento = (
            self.session.query(Rendimiento.idRendimiento)
            .filter(Rendimiento.idPasada == idPasada)
            .all()
        )
        return rendimiento

    def ConsultaDatosRendimiento(self, idRendimiento):
        self.session.commit()
        datos = (
            self.session.query(Rendimiento.Total, Rendimiento.Suprema, Rendimiento.Primera, Rendimiento.Segunda, Rendimiento.Tercera, Rendimiento.Cuarta)
            .filter(Rendimiento.idRendimiento == idRendimiento)
            .first()
        )
        return datos
    
    def ConsultaUltimaPasada(self, idCosecha):
        self.session.commit()
        pasada =(
            self.session.query(Pasada.idPasada)
            .filter(Pasada.idCosecha == idCosecha)
            .order_by(Pasada.idPasada.desc())
            .first()
        )
        return pasada[0]
    
    def ConsultaNombreRancho(self, nombreRancho):
        repeated = (
            self.session.query(Rancho.NombreRancho)
            .filter(Rancho.NombreRancho == nombreRancho)
            .first()
        )
        return repeated is not None
    
    def InsertarRancho(self, data, idCliente):
        registro = Rancho(
            NombreRancho = data["Rancho"],
            Pais = data["Pais"],
            Estado = data["Estado"],
            Localidad = data["Localidad"],
            Direccion = data["Direccion"],
            CoordenadasRancho = data["Coordenadas"],
            idCliente = idCliente
        )

        self.session.add(registro)
        self.session.commit()

    def ConsultaNombreVariedad(self, nombreVariedad):
        repeated = (
            self.session.query(Variedad.Nombre)
            .filter(Variedad.Nombre == nombreVariedad)
            .first()
        )
        return repeated is not None
    
    def InsertarVariedad(self, data: dict):
        registro = Variedad(
            Nombre = data["Variedad"],
            TiempoMaduracion = data["Maduracion"],
            TamanoPromedio = round(float(data["Tamano"]), 2),
            CostoPorHectareaPlantada = int(data["Costo"]),
        )
        self.session.add(registro)
        self.session.commit()

    def ConsultaNombreParcela(self, nombreParcela, idRancho):
        repeated = (
            self.session.query(Parcela.NombreParcela)
            .filter(Parcela.NombreParcela == nombreParcela, Parcela.idRancho == idRancho)
            .first()
        )
        return repeated is not None
    
    def InsertarParcela(self, data, idRancho, idVariedad):
        registro = Parcela(
            NombreParcela = data["Parcela"],
            TamanoHectarea = round(float(data["Tamano"]), 4),
            FechaPlantacion = data["Fecha"],
            CantidadPlantada = int(data["Cantidad"]),
            SeparacionEntreCultivo = round(float(data["Separacion"]), 2),
            DistanciaEntreSurcos = round(float(data["Distancia"]),2),
            CoordenadasParcela = data["Coordenadas"],
            EstadoParcela = data["Estado"],
            idRancho = idRancho,
            idVariedad = idVariedad,
        )
        self.session.add(registro)
        self.session.commit()
    
    def InsertarCosecha(self, data, idRancho, idParcela, idMaquina):
        registro = Cosecha(
            InicioCosecha = data["Fecha"],
            Nota = data["Nota"],
            idRancho = idRancho,
            idParcela = idParcela,
            idMaquina = idMaquina,
        )
        self.session.add(registro)
        self.session.commit()
    
    def ConsultaUltimaCosecha(self, fecha, idRancho, idParcela, idMaquina):
        self.session.commit()
        
        idCosecha = (
            self.session.query(Cosecha.idCosecha)
            .filter(Cosecha.InicioCosecha == fecha, Cosecha.idParcela == idParcela, Cosecha.idRancho == idRancho, Cosecha.idMaquina == idMaquina)
            .first()
        )
        return idCosecha

    def InsertarNuevaPasada(self, idCosecha, tiempoInicio):
        registro = Pasada(
            idCosecha = idCosecha,
            InicioPasada = tiempoInicio
        )
        self.session.add(registro)
        self.session.commit()
    
    def FinalizarPasada(self, idPasada, tiempoFinal):

        rel = update(Pasada).where(Pasada.idPasada == idPasada).values({"FinPasada": tiempoFinal})
        self.session.execute(rel)
        self.session.commit() 

    def ConsultaDefaultData(self, idCliente):
        self.session.commit() 
        default = (
            self.session.query(DefaultData)
            .filter(DefaultData.idCliente == idCliente)
            .first()
        )
        return default
    
    def UpdateDefaultdata(self, idCliente, data):
        rel = (
            update(DefaultData)
            .where(DefaultData.idCliente == idCliente)
            .values(
                idRancho = data["idRancho"],
                Rancho = data["Rancho"],
                idVariedad = data["idVariedad"],
                Variedad = data["Variedad"],
                idParcela = data["idParcela"],
                Parcela = data["Parcela"],
                idCosecha = data["idCosecha"],
            )
        )

        self.session.execute(rel)
        self.session.commit() 
    
    def InsertarDefaultData(self, idCliente, data):
        registro = DefaultData(
            idCliente = idCliente,
            idRancho = data["idRancho"],
            Rancho = data["Rancho"],
            idVariedad = data["idVariedad"],
            Variedad = data["Variedad"],
            idParcela = data["idParcela"],
            Parcela = data["Parcela"],
            idCosecha = data["idCosecha"],
        )
        self.session.add(registro)
        self.session.commit()


if __name__ == '__main__':
    from datosConexionBD import Datos as data
    Datos = data
    obj = Creacion(Datos)

    a = obj.ConsultaRanchoID(1).NombreRancho

    ic(type(a))
    ic(a)
    #print((a[0]))
    #print((a.idRendimiento))
    """ ranchos = obj.ConsultaRancho(5)
    #print(ranchos[0])
    for casa in ranchos:
        print(f"{casa}") """