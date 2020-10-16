Uma forma de criar é rodando o comando:

<code>php artisan make:controller NameController</code>

Se quiser que ele já gere seus métodos e funcione como recurso, execute este:

- <code>php artisan make:controller NameController -r</code> 
- <code>php artisan make:controller NameController -resource</code> 

Se quiser já injetar dependência de uma model pode utilizar dessas formas:

- <code>php artisan make:controller NameController --m=YourModel</code> 
- <code>php artisan make:controller NameController --model=YourModel</code> 

Além disso dá pra combinar as ideias acima:

- <code>php artisan make:controller NameController -r --m=YourModel</code> 
- <code>php artisan make:controller NameController -r --model=YourModel</code> 
- <code>php artisan make:controller NameController -resource --m=YourModel</code> 
- <code>php artisan make:controller NameController -resource --model=YourModel</code> 
