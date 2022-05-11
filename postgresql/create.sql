CREATE TABLE if not exists device_interface_configuration (
    id SERIAL PRIMARY KEY,
    connection INTEGER,
    name VARCHAR(255) NOT NULL,
    description VARCHAR(255),
    config json,
    type VARCHAR(50),
    infra_type VARCHAR(50),
    port_channel_id INTEGER,
    max_frame_size INTEGER
);