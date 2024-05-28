.data
str_nl: .asciz "\n"
.text
j Lmain
L0:
	sw ra, -0(sp)
L1:
	lw t1, -12(sp)
	lw t0, -4(sp)
	addi t0, t0, -12
	lw t2, 0(t0)
	rem t1, t1, t2
	sw t1, -20(sp)
L2:
	lw t1, -20(sp)
	lw t0, -4(sp)
	addi t0, t0, -16
	sw t1, 0(t0)
L3:
	lw t0, -8(sp)
	lw t0, -4(sp)
	addi t0, t0, -16
	lw t1, 0(t0)
	sw t1, 0(t0)
	lw ra, (sp)
	jr ra
L4:
	lw ra, 0(sp)
	addi sp, sp, 24
	jr ra
Lmain:
	addi sp, sp, -8
	mv fp, sp
L5:
	li t1, 4
	lw t0, -4(sp)
	addi t0, t0, -12
	sw t1, 0(t0)
L6:
	li t1, 10
	sw t1, -12(sp)
L7:
L8:
L9:
	addi fp, sp, -24
	lw t0, -4(sp)
	addi t0, t0, -12
	lw t0, 0(t0)
	sw t0, -12(fp)
L10:
	addi t0, sp, -20
	sw t0, -8(fp)
L11:
	sw sp, -4(fp)
	addi sp, sp, -24
	jal L0
	addi sp, sp, 24
L12:
L13:
	lw t0, -4(sp)
	addi t0, t0, -16
	sw t1, 0(t0)
L14:
	lw t0, -4(sp)
	addi t0, t0, -16
	lw a0, 0(t0)
	li a7, 1
	ecall
	la a0, str_nl
	li a7, 4
	ecall
L15:
	li a0, 0
	li a7, 10
	ecall
