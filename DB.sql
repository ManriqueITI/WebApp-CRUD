create database carrerasUniversitarias;
use carrerasUniversitarias;

CREATE TABLE registros (
    id INT AUTO_INCREMENT primary key,
    carrera varchar(50),
    descripcion varchar(300),
    cuatrimestres int(2)
);
INSERT INTO registros (`id`,`carrera`, `descripcion`, `cuatrimestres`) VALUES ('1','Administracion', 'Es la ciencia que permite a las empresas lograr sus fines dentro de un contexto global, diseñando estrategias que permitan evaluar su desarrollo y adaptarse a los cambios a través de técnicas que optimizan el uso de los recursos humanos, financieros y tecnológicos', '12');
