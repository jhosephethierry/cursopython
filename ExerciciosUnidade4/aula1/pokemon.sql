PGDMP     *                    {            Pokemons    15.2    15.2     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    32964    Pokemons    DATABASE     �   CREATE DATABASE "Pokemons" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Portuguese_Brazil.1252';
    DROP DATABASE "Pokemons";
                postgres    false            �            1259    32965    Pokedex    TABLE       CREATE TABLE public."Pokedex" (
    "Número Pokedex" integer NOT NULL,
    "Espécie" character varying(255),
    "Altura" character varying(255),
    "Peso" character varying(255),
    "Tipo" character varying(255),
    "Região" character varying(255)
);
    DROP TABLE public."Pokedex";
       public         heap    postgres    false            �          0    32965    Pokedex 
   TABLE DATA           g   COPY public."Pokedex" ("Número Pokedex", "Espécie", "Altura", "Peso", "Tipo", "Região") FROM stdin;
    public          postgres    false    214          e           2606    32971    Pokedex Pokedex_pkey 
   CONSTRAINT     e   ALTER TABLE ONLY public."Pokedex"
    ADD CONSTRAINT "Pokedex_pkey" PRIMARY KEY ("Número Pokedex");
 B   ALTER TABLE ONLY public."Pokedex" DROP CONSTRAINT "Pokedex_pkey";
       public            postgres    false    214            �   N  x�uXM��8\�O1��0`~�2'8�`��K�N?%�!��,�J�.s{Q��唕T;5�֌���쯘���!""�D����t?{TT��R�6�u�����
I7��f��U���$�2��3o7��U$r*���v1}��r����ZMz�I��X௛���8q,���.�'8;;��Ε�FSB1��kcx��I�B0˽)ƿ	�ݜ�|�Qb��u��C�嵓���)~��^!x�B�K8Ӷ���<e4�����W҆��+�N��c�s`�	�'��V�SӤ&Ň{�6�El5[O��q������'qL��x'�'TB�F^�Ȟ�r{g3�V���յ�)�,"0�:9s}�3�°���:��Mpl�~�Ɯ%v��X�`�]_�(�7�u���'��E䧷p��v����Z#����o�muk"%�F�J������ym���>��VߔqB�#���˚���kB)���s�������H�w�H@l�#![=�j�K�m�]��v�	�q�wH� 61�%��~;�����&�=cO�4�ڶ�A�z��lU0 N��:�ǭ��*�s��/�ꡝ;�� >� 
ϑV؋�bEm�|5���r��,��W���RZzLg��UB�g���T�n�4Q���y"Us�l����1��>�|J�^=dB�v�Q����7{JøT���mE��5���y+D1�BsF(hw������U7��uJ�ЙN�Ao� ����L�������tU�f�?�E&Rk��������jm�[KB��,^���L� �3KH]���}\�͏�e\�*o�E�#@�j�]}��9�"V!�Cym��A����y�<:A���SL0Tfݶ� �L�vzު@YQ��3�㖝�b.�hPy�d���0�I���Z�"�髵`��f^oՉS �Ѷ�+��:{��{W�P���-�簌�;�$��hl�������>t�l��	��4��1��Ci�^'��?����|�`h�T���L�)��q����E��&��>�>Tw�ӵ��z�C�P�T!��ǩ�?�$�X���*�Q��ְIͩҏ�r�̹�lvs}��`ɀ�8P)9T���n��Xl�����4��.��B��:��q�]r�p��;N;˄5�~�������"�OA�l����✚�
�������R��,C��
z��;u�,�ՅAI���Z��`��˶�(.����OD���V��T��I��u}�'��/	�{*�d����OZ�ϤB1l����T��A	���s�Rv�"ʨ1Sg�V{�M�PJE�?A�ܞ�B� GTA����43���"B�����"O6e��b�m����@�fi��.��q<]^��a�A�����ُ��<��C
��9'�׺]�Pn7�K���sT0�Q�q0�Z�v��T�zX*��1�p0�!�>�b�K~{m�1j�#0����⧔4py҂�3~N-�R-p���ݙN�=�O��u���x]���,���܋�����A)��Rs�O�Y�.���6��(�����4�_1ϴ�hVWd�������^����0yai�n���edA�\a�[��.&��j��g�O���V�'o�Ё'h~��Ҿ�2	sח��kы׏��7���T�����*�B��b�[j�~r�@A���ϭ���!L�-�N@8���H��S�xB�q��Q1)�U�ii�(��ap1�F�UPj(͎Y����\g�%9(�z���H�V�۷�M�C ؊�pz��5U!
� �;��ǿ���P�|��c��I)�O�cB��J����2:��v-/�I��s=x�:����ׯ_�I��     