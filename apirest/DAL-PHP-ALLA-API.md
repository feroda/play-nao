# Effettuare richieste HTTP direttamente da PHP

Utilizzeremo una libreria che si chiama `libcurl` dovrebbe essere già installata su Ubuntu,
altrimenti proveremo ad installarla con `apt-get` come sappiamo fare.

Poi utilizzeremo questa funzione:

```
<?php 
// DO REST HTTP REQUEST with json payload
function do_rest($method,$url,$json=NULL,$options=NULL) {
  global $http_handle,$adb_option_defaults;

  // Connect
  if(!isset($http_handle)) $http_handle = curl_init();

  //DEBUG
  echo "DB operation: $method $url $json\n";

  // Compose querry
  $options = array(
    CURLOPT_URL => $url,
    CURLOPT_CUSTOMREQUEST => $method, // GET POST PUT PATCH DELETE HEAD OPTIONS
    CURLOPT_POSTFIELDS => $json,
  );
  curl_setopt_array($http_handle, $options);

  // send request and wait for response
  $response =  json_decode(curl_exec($http_handle),true);

  echo "Response from REST API: \n";
  print_r($response);

  return($response);
}
?>
```

(originariamente presa da: http://php.net/manual/en/curl.examples-basic.php#112076)

Esempi di utilizzo:

```
do_rest("GET", "https://maps.googleapis.com/maps/api/geocode/json?address=fabriano,an");
```
