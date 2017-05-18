# Dotare NAO di una API REST

## Cosa si intende per API REST?

**API** = con Application Program Interface si intende una interfaccia esposta da un'aplicazione per essere contattata da altri programmi. Nel caso delle applicazioni di rete, questo rende l'applicazione un servizio di rete.

**REST** = Representional State Transfer, consiste in un'insieme di convenzioni che definiscono una architettura per le applicazioni di rete. Se tali applicazioni seguono queste convenzioni, ad oggi diffusissime nella realizzazione di servizi web, vengono dette RESTful.

I vincoli dell'approccio architetturale REST sono:

 * **client/server**: separazione dei ruoli tra client e server che interagiscono tramite una interfaccia uniforme;
 * **uniform interface**: l'interfaccia di comunicazione tra client e server deve essere omogenea
 * **stateless**: il server non memorizza lo stato del client, ciò significa che da ogni richiesta è possibile ricostruire esattamente la situazione sul server
 * **cacheable**: si possono attuare meccanismi di caching delle risposte secondo le indicazioni contenute nelle risposte stesse
 * **layered system**: possono esserci sistemi intermedi tra il client e il server

Il concetto di **REST** non è strettamente legato ad [HTTP](https://it.wikipedia.org/wiki/HTTP), ma il suo uso più diffuso oggi è con questo protocollo. Leggi: oggi i servizi web vengono implementati con l'architettura REST (esempi su API GoogleMaps, Instagram, Spotify, ...)

Questa architettura ci consente di sviluppare applicazioni orientate ai servizi (SOA) in cui ciascun servizio coopera con altri per offrire all'utente un risultato migliore che agendo da solo. O senza alcuno di questi criteri.

Approfondimenti su [Wikipedia Italia pagina REST](https://it.wikipedia.org/wiki/Representational_State_Transfer)

## Le risorse

Ruolo centrale nell'architettura REST è assunto dalle **risorse**, di cui l'HTTP trasferisce delle rappresentazioni di solito nel body delle risposte in formato **JSON** o **XML**.

Come vengono mappate su HTTP le operazioni CRUD (= Create, Read, Update, Delete)?

 * POST -> C = CREATE = aggiunge una risorsa alla collezione identificata dall'URI
 * GET  -> R = READ   = recupera informazioni sulla risorsa identificata dall'URI (sia essa una collezione o un elemento)
 * PUT  -> U = UPDATE = aggiorna la risorsa identificata dall'URI (sia essa una collezione o un elemento)
 * DELETE -> D = DELETE = elimina la risorsa identificata dall'URI (sia essa una collezione o un elemento)

[Passa a leggere l'esperimento](ESPERIMENTO.md)
