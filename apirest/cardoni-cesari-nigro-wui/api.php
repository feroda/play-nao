
<html>

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

do_rest("PUT", "http://192.168.10.12:8080/api/v1/languages/".$_POST["lingua"], "{"active": true}");
do_rest("POST", "http://192.168.10.12:8080/api/v1/text2speech/", { "action": "say", "text": $_POST["parola"] });

echo "La lingua selezionata e'".$_POST["lingua"]."e la frase detta e'".$_POST["parola"];

?>

</html>
