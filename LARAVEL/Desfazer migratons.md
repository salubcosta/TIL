Para desfazer uma migrations que acabou de criar. Utilize este comando:

<code>
php artisan migrate:rollback
</code>


Também é possível escolher quantos passos você quer desfazer. Exemplo:

<code>
php artisan migrate:rollback --step=3
</code>


Da forma como está acima, será desfeito 3 passos de migrate. 
Lembrando que a cada migration é salvo os registros na tabela migration, cujos campos são: ID, MIGRATION e BATCH
