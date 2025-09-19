DROP SCHEMA IF EXISTS shotbase CASCADE;
CREATE SCHEMA shotbase;

--------------------------------------------------------------
-- Table admin
--------------------------------------------------------------

DROP TABLE IF EXISTS shotbase.admin CASCADE ;
CREATE TABLE shotbase.admin (
    id_admin serial PRIMARY KEY,
    identifiant_admin VARCHAR(50) UNIQUE NOT NULL,
    mot_passe CHAR(10) UNIQUE NOT NULL
);


--------------------------------------------------------------
-- PARTICIPANTS
--------------------------------------------------------------

DROP TABLE IF EXISTS shotbase.participants CASCADE ;

CREATE TABLE tp.participants (
    id_participant SERIAL PRIMARY KEY,
    email VARCHAR(50) UNIQUE NOT NULL,
    nom VARCHAR(50) NOT NULL,
    prenoms VARCHAR(100) NOT NULL,
    date_creation_compte DATE,
    etudiant_ensai BOOLEAN UNIQUE NOT NULL,
    mot_passe_client CHAR(10) UNIQUE NOT NULL
);


--------------------------------------------------------------
-- Types de Pokemons
--------------------------------------------------------------

DROP TABLE IF EXISTS tp.pokemon_type CASCADE ;

CREATE TABLE tp.pokemon_type (
    id_pokemon_type serial PRIMARY KEY,
    pokemon_type_name text UNIQUE NOT NULL,
    pokemon_type_description text
);


--------------------------------------------------------------
-- Pokemons
--------------------------------------------------------------

DROP TABLE IF EXISTS tp.pokemon CASCADE;

CREATE TABLE tp.pokemon (
    id_pokemon_type integer REFERENCES tp.pokemon_type(id_pokemon_type),
    name text UNIQUE NOT NULL,
    id_pokemon serial PRIMARY KEY,
    level integer,
    hp integer,
    attack integer,
    defense integer,
    spe_atk integer,
    spe_def integer,
    speed integer,
    url_image text
);

-- Comme on va creer des pokemon en forcant les id_pokemon
-- il faut maj a la main la valeur de la sequence de la PK
ALTER SEQUENCE tp.pokemon_id_pokemon_seq RESTART WITH 899;


--------------------------------------------------------------
-- Attaques des Pokemons
--------------------------------------------------------------

DROP TABLE IF EXISTS tp.pokemon_attack CASCADE;

CREATE TABLE tp.pokemon_attack (
    id_pokemon integer REFERENCES tp.pokemon(id_pokemon) ON DELETE CASCADE,
    id_attack integer REFERENCES tp.attack(id_attack) ON DELETE CASCADE,
    level integer,
    PRIMARY KEY (id_pokemon, id_attack)
);