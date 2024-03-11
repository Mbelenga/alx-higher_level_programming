#!/usr/bin/node
const arg = parseInt(process.argv[2]);
if (arg) {
	console.log('My number: ${firstarg}');
} else {
	console.log("Not a number");
}
