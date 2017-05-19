
<html>
<head>
</head>
<body>

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

$NAO_BASE_URL="http://192.168.10.12:8080/";

if (isset($_POST["parola"])) {
    $lingua=$_POST["lingua"];
    $frase=$_POST["parola"];
} else {
    $lingua="Italian";
    $frase="Ciao mondo... per prova ";
    $frase.="dato che probabilmente mi stai lanciando da una GET o da linea di comando";
}

do_rest("PUT", $NAO_BASE_URL."api/v1/languages/".$lingua, '{ "active": true }');
do_rest("POST", $NAO_BASE_URL."api/v1/text2speech/", '{ "action": "say", "text": $_POST["parola"]}');

echo "La lingua selezionata e' ".$lingua." e la frase detta e' ".$frase;

?>

</body>
</html>
