// var divs = document.querySelectorAll('div.text-sm.dark\\:text-zinc-300');

// // Update class attribute for each selected div
// divs.forEach(div => {
//     div.classList.remove('hidden'); // Remove the 'false' class
//      // Add the 'hidden' class
// });



//  SAVED NOTES -> OPEN DSA SHEET




let processNotes = (noteRow) => {
    let fileName = noteRow.parentElement.parentElement.getElementsByTagName('td')[1].textContent
	let topicName = noteRow.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.getElementsByTagName("button")[0].getElementsByTagName("div")[0].textContent
    topicName = topicName.split(": ")[1]
    console.log(topicName);

    let txtArea = noteRow.getElementsByTagName("textarea")
    if ((txtArea[0] != undefined) && (txtArea[0].innerText != "")) {
        let cleanText = txtArea[0].innerText.replace(/<br>/g, '\n').replace(/\u00A0/g, ' ');

        return {
            "fileName": fileName.trim().replaceAll(" ","_"),
            "data": cleanText,
            "topic": topicName
        }
    }

    return null
}

let openNoteRows = Array.from(document.querySelectorAll(".border-t-2"))
let dataItems = openNoteRows.map(x => processNotes(x))

// keep only filled notes
let dataItemsFiltered = dataItems.filter(x => ((x != null) && (x.data !== "\n\n\n")))


// download json
var jsonContent = JSON.stringify(dataItemsFiltered);
var blob = new Blob([jsonContent], { type: 'application/json' });
var a = document.createElement('a');
a.href = URL.createObjectURL(blob);
a.download = 'cleaned_items.json';
document.body.appendChild(a);
a.click();
document.body.removeChild(a);

