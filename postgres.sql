CREATE DATABASE "test-1" WITH ENCODING = 'UTF8'

CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,                    
    nombre VARCHAR(100) NOT NULL,            
    correo VARCHAR(100) UNIQUE NOT NULL,      
    create_at TIMESTAMPTZ DEFAULT NOW(),
    update_at TIMESTAMPTZ,
    delete_at TIMESTAMPTZ 
);


INSERT INTO usuarios (nombre, correo) 
VALUES 
    ('test', 'test@example.com'),
    ('Pepe Pepe', 'pepe@example.com'),
    ('Lalo Lalo', 'lalo@example.com');
    
SELECT *
FROM usuarios
WHERE created_at ::DATE >= CURRENT_DATE - INTERVAL '7 days'
ORDER BY created_at DESC;