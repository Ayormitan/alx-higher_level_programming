#!/usr/bin/node
/**
 * prints argument to console
 */
const argv = process.argv.slice(2)
if (argv[0])
{
	console.log('argv[0]');
}
else
{
	console.log('No argument');
}
