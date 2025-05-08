# https://wanglab.hosted.uark.edu/LearningPerl/www.unix.org.ua/orelly/perl/learn/examples/index.htm

#!/usr/bin/perl -w

use strict;
use warnings;

sub hello {
	print("Hello world!\n");
	my $var = $_[0];
	print("I am $var $_[1]. And you ?\n\n");
}

sub guess_name {
	my $my_name=<STDIN>;
	chomp($my_name);

	print("You wanna play ? ");
	my $answ = <STDIN>;
	chomp($answ);

	#my $my_name=$_[0];
	#chomp($my_name);

	if($answ eq "no"){
		print("So, I am $_[0].");
	}else{
		print("Then, guess it.");
		my $guess = <STDIN>;
		while($guess ne $my_name){
			print("Wrong, try again. ");
			my $guess = <STDIN>;
			chomp($guess);
		}
	}
}

sub operators_strings {
	print "Hello"." "."Lilly\n";
	print "Lilly " x 3;
	#print (3+2) x 4;
	
	my $test = "LillyS";
	chop($test);
	print "\n$test";
	
}

sub circ {
	my $pi = 3.141592654;
	return 2*$pi*$_[0];
}

sub list {
	#my $test = (1,2,3);
	print (1..5);
	my @a = qw(Lilly Smith smililly);
	#print "\n @a[1]";
	(my $a, my $b, my $c)=(1..3);
	print "\n $b";
	print "\n \n";


	my @superlist = (3..7);
	unshift(@superlist,0);
	print "\n @superlist";
	my $x = shift(@superlist);
	print "\n @superlist";
	#print reverse(@superlist);
	
	print "\n @superlist[1,3]";


	#@a = <STDIN>;

}

sub stack {
	my @mylist = ();
	push(@mylist, 0);
	push(@mylist, 2);
	#print @mylist;
	my $value = pop(@mylist);
	#print $value;
	print @mylist;

}

sub random {
	my $min = $_[0];
	my $max = $_[1];

	return int(rand($max-$min)) + $min;

}

sub lists {
	my @superlist = ("hello", "smililly", "Luv", "U");
	#print @superlist[2];

	srand;
	print $superlist[rand(@superlist)];

	my $vrand = rand();
	print "\n $vrand";

	my $vrand = rand(10);
	print "\n $vrand \n\n";

	my $i = 0;
	for($i=1 ; $i <= 5; $i++){
		print random(2, 12);
	}

	
	print("\n");
	my @a = (1..5);
	foreach $b (reverse @a){
		print $b ;
	}

}

#hello("Lilly", "Smith");
#guess_name("smililly");

#operators_strings();

#print circ(12.5);

#list();
#stack();
lists();

 

