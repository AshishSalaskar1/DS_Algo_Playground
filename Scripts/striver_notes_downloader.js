// let processNotes = (openNoteBtn) => {
// 	// console.log(openNoteBtn)
// 	// get fileName before clicking on notesOpen button
// 	let fileName = openNoteBtn.parentElement.parentElement.getElementsByTagName('td')[1].textContent
// 	let topicName = openNoteBtn.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.getElementsByTagName("summary")[0].textContent.trim()
// 	topicName = topicName.match(/:\s*(.+)\s*\(\d+\/\d+\)/)[1];



// 	openNoteBtn.click() // open button
// 	let cleanText = document.getElementsByClassName("notes__view")[0].innerText
// 	    .replace(/<br>/g, '\n').replace(/\u00A0/g, ' ');
// 	document.getElementById("close-notes-btn").click() // close current window
	
// 	return {
// 		"fileName": fileName.trim().replaceAll(" ","_"),
// 		"data": cleanText,
// 		"topic": topicName
// 	}

// }


// // click all plus icons
// Array.from(document.getElementsByTagName("details")).map(x=>x.toggleAttribute("open"))

// // get all notes open buttons and extract data
// let openNoteBtns = Array.from(document.querySelectorAll('td[title="View/Edit Note"] button:first-child, td[title="Add Note"] button:first-child'));
// let dataItems = openNoteBtns.map(x => processNotes(x))

// // keep only filled notes
// let dataItemsFiltered = dataItems.filter(x => x.data !== "\n\n\n")


// // download json
// var jsonContent = JSON.stringify(dataItemsFiltered);
// var blob = new Blob([jsonContent], { type: 'application/json' });
// var a = document.createElement('a');
// a.href = URL.createObjectURL(blob);
// a.download = 'cleaned_items.json';
// document.body.appendChild(a);
// a.click();
// document.body.removeChild(a);

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