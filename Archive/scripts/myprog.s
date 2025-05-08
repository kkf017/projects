arm-linux-gnueabi-gcc myprogram.s
qemu-arm- -L /usr/arm-linux-gnueabi a.out

si ça ne marche pas
sudo apt-get install gcc-a
sudo apt get install qemu-user


Si librairie printf n'est pas trouvée
readelf -l a.out



	.data
str:	.asciz	"Hello, world.\n"

	.text
	.globl	main

main: 	stmfd	sp!,{lr}
	ldr	r0,=str
	bl	printf
	mov	r0,#0
	ldmfd	sp!,{lr}
	mov	pc,lr
