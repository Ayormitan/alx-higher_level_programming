#!/usr/bin/node
/**
 * Using process arg
 * fiels
 */
const args = process.argv;

if (args.length <= 2) {
	console.log('No argument');
}
else{
	console.log('Argument found');
}
