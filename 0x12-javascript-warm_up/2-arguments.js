#!/usr/bin/node
/**
 * Using process arg
 */
const args = process.argv;
	if (args.length <= 2)
	{
		console.log('No argument found');
	}
	else
	{
		console.log('Argument found');
	}
