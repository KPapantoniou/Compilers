.data
str_nl: .asciz "\n"
.text
j Lmain
L0:
	sw ra, -0(sp)
L1:
	lw t0, -4(sp)
	lw t0, -4(t0)
	addi t0, t0, -12
	lw t1, 0(t0)
	li t2, 1
	add t1, t1, t2
	sw t1, -20(sp)
L2:
	#before for loadvr
	lw t1, -20(sp)
	#here for loadvr
	lw t0, -4(sp)
	lw t0, -4(t0)
	addi t0, t0, -16
	sw t1, 0(t0)
	#here for storevr
L3:
	lw t0, -4(sp)
	lw t0, -4(t0)
	addi t0, t0, -16
	lw t1, 0(t0)
	lw t0, -4(sp)
	lw t0, -4(t0)
	addi t0, t0, -12
	lw t2, 0(t0)
	add t1, t1, t2
	sw t1, -24(sp)
L4:
	#before for loadvr
	lw t1, -24(sp)
	#here for loadvr
	sw t1, -16(sp)
	#here for storevr
L5:
	lw a0, -16(sp)
	li a7, 1
	ecall
	la a0, str_nl
	li a7, 4
	ecall
L6:
	lw t0, -8(sp)
	lw t0, -4(sp)
	lw t0, -4(t0)
	addi t0, t0, -16
	lw t1, 0(t0)
	sw t1, 0(t0)
	lw ra, (sp)
	addi sp, sp, 28
	jr ra
L7:
	lw ra, 0(sp)
	addi sp, sp, 28
	jr ra
Lmain:
	addi sp, sp, -8
	mv fp, sp
L8:
	li a7, 5
	ecall
	add t1, zero, a0
	sw t1, -12(sp)
	sw a0, -12(sp)
L9:
L10:
L11:
	addi fp, sp, -28
	lw t0, -12(sp)
	sw t0, -12(fp)
L12:
	addi t0, sp, -12
	sw t0, -8(fp)
L13:
	lw t0, -4(sp)
	sw t0, -4(fp)
	addi sp, sp, -28
	jal L0
	addi sp, sp, 28
L14:
L15:
	#before for loadvr
	#here for loadvr
	sw t1, -16(sp)
	#here for storevr
L16:
	lw a0, -16(sp)
	li a7, 1
	ecall
	la a0, str_nl
	li a7, 4
	ecall
L17:
	li a0, 0
	li a7, 10
	ecall
