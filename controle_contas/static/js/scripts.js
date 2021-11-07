// JS Sources

function getFormCreate(){
    let modalBody = document.querySelector("#modalCreateForm")

    fetch("add-sources", {
        method: "GET",
        credentials: "include",
        })
    .then(response => {response.text()
    .then(data => modalBody.innerHTML = data)})
    .catch(e => console.log("deu ruim"))
}

function createSource(){

    let csrfToken = document.querySelector("#csrf_token")
    let description = document.querySelector("#description")

    let formData = new FormData()

    formData.append("csrf_token", csrfToken.value)
    formData.append("description", description.value)

    fetch("add-sources", {
        method: "POST",
        credentials: "include",
        body: formData
    })
    .then(response => {response.json()
    .then(data => console.log(data))
    document.location.reload(true)
        })
    .catch(e => console.log("deu ruim"))
}


function getFormEdit(pk=0){
    let modal = document.querySelector("#editSources")
    let modalBody = document.querySelector("#modalEditForm")

    fetch(`edit-sources/${pk}`, {
        method: "GET",
        credentials: "include",
    })
    .then(response => {response.text()
    .then( data => modalBody.innerHTML = data)
    })
    .catch(e => console.log("deu ruim"))

}

function submitEditForm(pk=0){

    let csrfToken = document.querySelector("#csrf_token")
    let description = document.querySelector("#description")
    let formData = new FormData()
    formData.append("csrf_token", csrfToken.value)
    formData.append("description", description.value)
    console.log(description.value)

    fetch(`edit-sources/${pk}`, {
        method: "POST",
        credentials: "include",
        body: formData
    })
    .then(response => {
        response.text()
        .then(data => console.log(data))
        document.location.reload(true)
    })
    .catch(e => console.log("deu ruim"))
    
}

function delItem(pk=0){
    fetch(`del-sources/${pk}`, {
        method: "GET",
        credentials: "include",
    })
    .then(response => {
        response.json()
        .then( data => console.log(data))
        document.location.reload(true)
    })
    .catch(e => console.log("deu ruim"))
}
    
// JS Entry

function getFormCreateEntry(){
    let modalBody = document.querySelector("#modalCreateForm")

    fetch("add-entries", {
        method: "GET",
        credentials: "include",
        })
    .then(response => {response.text()
    .then(data => modalBody.innerHTML = data)})
    .catch(e => console.log("deu ruim"))
}

function createEntries(){


    let csrfToken = document.querySelector("#csrf_token")
    let description = document.querySelector("#description")
    let value = document.querySelector("#value")
    let quantum = document.querySelector("#quantum")
    let idSource = document.querySelector("#id_source")
    let revenue = document.querySelector("#revenue")

    if (revenue.checked){
        revenue.value = "y"
        console.log(revenue.value)
    }else{
        revenue.value = ""
        console.log(revenue.value)
    }

    let formData = new FormData()

    formData.append("csrf_token", csrfToken.value)
    formData.append("description", description.value)
    formData.append("value", value.value)
    formData.append("quantum", quantum.value)
    formData.append("id_source", idSource.value)
    formData.append("revenue", revenue.value)

    fetch("add-entries", {
        method: "POST",
        credentials: "include",
        body: formData
    })
    .then(response => {response.text()
    .then(data => console.log(data))
    document.location.reload(true)
        })
    .catch(e => console.log("deu ruim"))
}


function getFormEditEntries(pk=0){
    let modal = document.querySelector("#editEntries")
    let modalBody = document.querySelector("#modalEditForm")

    fetch(`edit-entries/${pk}`, {
        method: "GET",
        credentials: "include",
    })
    .then(response => {response.text()
    .then( data => modalBody.innerHTML = data)
    })
    .catch(e => console.log("deu ruim"))

}

function submitEditFormEntries(pk=0){

    let csrfToken = document.querySelector("#csrf_token")
    let description = document.querySelector("#description")
    let value = document.querySelector("#value")
    let quantum = document.querySelector("#quantum")
    let idSource = document.querySelector("#id_source")
    let revenue = document.querySelector("#revenue")

    if (revenue.checked){
        revenue.value = "y"
        console.log(revenue.value)
    }else{
        revenue.value = ""
        console.log(revenue.value)
    }

    let formData = new FormData()

    formData.append("csrf_token", csrfToken.value)
    formData.append("description", description.value)
    formData.append("value", value.value)
    formData.append("quantum", quantum.value)
    formData.append("id_source", idSource.value)
    formData.append("revenue", revenue.value)

    fetch(`edit-entries/${pk}`, {
        method: "POST",
        credentials: "include",
        body: formData
    })
    .then(response => {
        response.text()
        .then(data => console.log(data))
        document.location.reload(true)
    })
    .catch(e => console.log("deu ruim"))
    
}

function delEntry(pk=0){
    fetch(`del-entries/${pk}`, {
        method: "GET",
        credentials: "include",
    })
    .then(response => {
        response.json()
        .then( data => console.log(data))
        document.location.reload(true)
    })
    .catch(e => console.log("deu ruim"))
}

// Invoices


function getDetailsInvoices(pk=0){

    let modalBody = document.querySelector("#modalDetail")

    fetch(`invoices-details/${pk}`, {
        method: "GET",
        credentials: "include",
    })
    .then(response => {response.text()
    .then( data => modalBody.innerHTML = data)
    })
    .catch(e => console.log("deu ruim"))
}



function delInvoices(pk=0){
    fetch(`del-invoices/${pk}`, {
        method: "GET",
        credentials: "include",
    })
    .then(response => {
        response.json()
        .then( data => console.log(data))
        document.location.reload(true)
    })
    .catch(e => console.log("deu ruim"))
}