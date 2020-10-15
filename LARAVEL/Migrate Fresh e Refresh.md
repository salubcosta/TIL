- <code>php artisan migrate:fresh</code>

Com este comando, ocorre um drop all tables e em seguida é recriado as tabelas.
Muito cuidado pois se as tabelas tiverem dados, haverá perdas

- <code>php artisan migrate:refresh</code>

Agora já com este, ele faz um rollback nas migrations e refaz as migrações.
