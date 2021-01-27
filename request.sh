 for i in {1..100}; 
 do 
    curl -XPOST -H "Content-Type: application/json" -d '{"name":"'$i' Todo"}' http://$1:8080/todos; 
done