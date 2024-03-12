#!/usr/bin/node
let count = 0;
exports.logMe = function (item) {
	consol .log(`${count++}: ${item}`);
}
