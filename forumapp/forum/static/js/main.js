//const socket = io();
let bbl;
let calendar = [];
let months = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:20,12:31};
let table;
let counter = 0;
var d = new Date();
var n = d.getMonth() + 1;
let day;
let dvs = [];
let opt;
var selector = document.getElementById('day');
var today = new Date();
var dd = String(today.getDate()).padStart(2, '0');
var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
var yyyy = today.getFullYear();
today = mm + '/' + dd + '/' + yyyy;

for (let i = 1; i <months[n]+1;i++) {
	opt = document.createElement('option');
	opt.value = i;
	opt.innerText= i;
	selector.append(opt);
}
selector;

class html_ele{
	constructor(amount,parentID,typele) {
		this.amount = amount;
		this.dvs = [];
		var element = document.getElementById(parentID);
		for (let i = 0; i<this.amount;i++) {
			this.element = document.getElementById(parentID);
			this.currele = document.createElement(typele);
			this.dvs.push(this.currele);
			document.getElementById(parentID).appendChild(this.currele);
		}
		//console.log('ele_div constructed succesfully');

	}	all_txt(text){
		for (let i = 0;i<this.dvs.length;i++){
			this.dvs[i].innerHTML = text;
		} 
		//console.log('ele_div all_txt method succesful');
		
	}	txt(text, pos) {
		this.dvs[pos].innerHTML = text; 
		//console.log('ele_div txt method succesful');
	}	giveId(ID){
		for (let i = 0; i<this.dvs.length;i++) {
			this.dvs[i].id = ID;
		}
	}	giveClass(Class){
		for (let i = 0; i<this.dvs.length;i++) {
			this.dvs[i].class = Class;
		}
	}
}

class Table {
	constructor() {
		this.table = document.createElement('table');
		this.table.id = 'calendar_table';
		this.tr_obj_arr = [];
		document.body.append(this.table);
	}	
	get tr_amount() {
		let tr_amount = this.table.childElementCount;
		return tr_amount;
	}
	create_tr(){
		this.tr = document.createElement('tr');
		this.table.append(this.tr);
		this.tr_obj_arr.push(this.tr);
		this.tr.id = `tr-${this.table.childElementCount}`;
	}
	get tr_objs() {
		return this.tr_obj_arr;
	}
}

table = new Table; 
table.create_tr();

function createbbl(username,date,AOT,desc,amount,day) {
	counter++;
	let curr_row = table.tr_objs[table.tr_objs.length-1];
	console.log(`parent id: td-${day}`)
	//let dv = new html_ele(1,`td-${day}`,'div');
	let dv = document.createElement('div');
	dvs.push(dv);
	document.getElementById(`td-${day}`).append(dv);
	dv.id = `div-${counter}`;
	dv.class = 'bbl';
	//dv.giveId(dv.id);
	bbl = new html_ele(amount,dv.id,'p');
	console.log(`div id: ${dv.id}`);
	let bbl_info = ['username: ' + username,'date: ' + date,'amount of time: ' + AOT, 'desc.: '+desc ];
	for (let i = 0; i<amount;i++) {
		bbl.txt(bbl_info[i],i);	

	}
}

function createdrop() {
	
}

function createCalendar() {
	console.log("days in the month:"+months[n]);
	for (let i=0; i<months[n];i++) {
		counter++;
		let td = document.createElement('td');
		calendar.push(td);
		td.id = `td-${counter}`;
		this.len = calendar.length;
		let curr_row = table.tr_objs[table.tr_objs.length-1];
		curr_row.append(td);
		if (this.len%6 == 0) {
			table.create_tr();
		}
	}
}
createCalendar();

function update() {
	let day = document.getElementById('day').value;
	let AOT = document.getElementById('AOT').value;
	let desc = document.getElementById('desc').value;
	createbbl('usr',today,AOT,desc,4,day);
}
//prevent refresh when submitted
var form = document.getElementById("form_cal");
function handleForm(event) { event.preventDefault(); } 
form.addEventListener('submit', handleForm);


