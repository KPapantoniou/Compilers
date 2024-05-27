.data
str_nl: .asciz "\n"
.text
j Lmain
L0:
	sw ra, 0(sp)
L1:
	lw t1, -12(sp)
	li t2, 1
	add t1, t1, t2
	lw t0, -4(sp)
	addi t0, t0, -28
	sw t1, 0(t0)
L2:
	lw t0, -4(sp)
	addi t0, t0, -28
	lw t1, 0(t0)
	sw t1, -12(sp)
L3:
	lw t0, -4(sp)
	lw t0, -12(sp)
	lw t0, 0(t0)
	lw t1, 0(t0)
	lw t0, -4(sp)
	lw t0, -16(sp)
	lw t0, 0(t0)
	lw t2, 0(t0)
	bgt t1, t2, L6
L4:
	j L10
L5:
	lw t0, -4(sp)
	lw t0, -12(sp)
	lw t0, 0(t0)
	lw t1, 0(t0)
	lw t0, -4(sp)
	lw t0, -20(sp)
	lw t0, 0(t0)
	lw t2, 0(t0)
	bgt t1, t2, L8
L6:
	j L10
L7:
	lw t0, -4(sp)
	lw t0, -12(sp)
	lw t0, 0(t0)
	lw t1, 0(t0)
	lw t0, -4(sp)
	addi t0, t0, -24
	sw t1, 0(t0)
L8:
	j L17
L9:
	lw t0, -4(sp)
	lw t0, -16(sp)
	lw t0, 0(t0)
	lw t1, 0(t0)
	lw t0, -4(sp)
	lw t0, -12(sp)
	lw t0, 0(t0)
	lw t2, 0(t0)
	bgt t1, t2, L12
L10:
	j L15
L11:
	lw t0, -4(sp)
	lw t0, -16(sp)
	lw t0, 0(t0)
	lw t1, 0(t0)
	lw t0, -4(sp)
	lw t0, -20(sp)
	lw t0, 0(t0)
	lw t2, 0(t0)
	bgt t1, t2, L14
L12:
	j L15
L13:
	lw t0, -4(sp)
	lw t0, -16(sp)
	lw t0, 0(t0)
	lw t1, 0(t0)
	lw t0, -4(sp)
	addi t0, t0, -24
	sw t1, 0(t0)
L14:
	lw t0, -4(sp)
	lw t0, -20(sp)
	lw t0, 0(t0)
	lw t1, 0(t0)
	lw t0, -4(sp)
	addi t0, t0, -24
	sw t1, 0(t0)
L15:
	lw t0, -8(sp)
	lw t0, -4(sp)
	addi t0, t0, -24
	lw t1, 0(t0)
	sw t1, 0(t0)
	lw ra, (sp)
	addi sp, sp, 32
	jr ra
L16:
	li a0, 0
	li a7, 10
	ecall
L17:
	sw ra, 0(sp)
L18:
	lw t1, -12(sp)
	li t2, 1
	add t1, t1, t2
	lw t0, -4(sp)
	addi t0, t0, -16
	sw t1, 0(t0)
L19:
	lw t0, -4(sp)
	addi t0, t0, -16
	lw t1, 0(t0)
	sw t1, -12(sp)
L20:
	lw t0, -4(sp)
	lw t0, -12(sp)
	lw t0, 0(t0)
	lw t1, 0(t0)
	li t2, 0
	blt t1, t2, L25
L21:
	j L27
L22:
	lw t0, -8(sp)
	li t1, -1
	sw t1, 0(t0)
	lw ra, (sp)
	addi sp, sp, 40
	jr ra
L23:
	j L42
L24:
	lw t0, -4(sp)
	lw t0, -12(sp)
	lw t0, 0(t0)
	lw t1, 0(t0)
	li t2, 0
	beq t1, t2, L31
L25:
	j L29
L26:
	lw t0, -4(sp)
	lw t0, -12(sp)
	lw t0, 0(t0)
	lw t1, 0(t0)
	li t2, 1
	beq t1, t2, L31
L27:
	j L32
L28:
	lw t0, -8(sp)
	li t1, 1
	sw t1, 0(t0)
	lw ra, (sp)
	addi sp, sp, 40
	jr ra
L29:
	lw t0, -4(sp)
	lw t0, -12(sp)
	lw t0, 0(t0)
	lw t1, 0(t0)
	li t2, 1
	sub t1, t1, t2
	lw t0, -4(sp)
	addi t0, t0, -20
	sw t1, 0(t0)
L30:
L31:
L32:
	addi fp, sp, 40
	lw t0, -4(sp)
	addi t0, t0, -20
	lw t0, 0(t0)
	sw t0, -12(fp)
L33:
	addi t0, sp, -24
	sw t0, -8(fp)
L34:
	sw sp, -4(sp)
	addi sp, sp, -40
	jal fib
	addi sp, sp, 40
	addi sp, sp, -40
	jal L20
L35:
L36:
	lw t0, -4(sp)
	lw t0, -12(sp)
	lw t0, 0(t0)
	lw t1, 0(t0)
	li t2, 2
	sub t1, t1, t2
	lw t0, -4(sp)
	addi t0, t0, -28
	sw t1, 0(t0)
L37:
L38:
L39:
	addi fp, sp, 40
	lw t0, -4(sp)
	addi t0, t0, -28
	lw t0, 0(t0)
	sw t0, -12(fp)
L40:
	addi t0, sp, -32
	sw t0, -8(fp)
L41:
	sw sp, -4(sp)
	addi sp, sp, -40
	jal fib
	addi sp, sp, 40
	addi sp, sp, -40
	jal L20
L42:
L43:
	add t1, t1, t2
	lw t0, -4(sp)
	addi t0, t0, -36
	sw t1, 0(t0)
L44:
	lw t0, -8(sp)
	lw t0, -4(sp)
	addi t0, t0, -36
	lw t1, 0(t0)
	sw t1, 0(t0)
	lw ra, (sp)
	addi sp, sp, 40
	jr ra
L45:
	li a0, 0
	li a7, 10
	ecall
L46:
	sw ra, 0(sp)
L47:
	lw t1, -12(sp)
	li t2, 1
	add t1, t1, t2
	lw t0, -4(sp)
	lw t0, -4(t0)
	addi t0, t0, -20
	sw t1, 0(t0)
L48:
	lw t0, -4(sp)
	lw t0, -4(t0)
	addi t0, t0, -20
	lw t1, 0(t0)
	sw t1, -12(sp)
L49:
	lw t0, -4(sp)
	lw t0, -4(t0)
	lw t0, -16(sp)
	lw t0, 0(t0)
	lw t1, 0(t0)
	lw t0, -4(sp)
	lw t0, -4(t0)
	lw t0, -12(sp)
	lw t0, 0(t0)
	lw t2, 0(t0)
	div t1, t1, t2
	lw t0, -4(sp)
	lw t0, -4(t0)
	addi t0, t0, -24
	sw t1, 0(t0)
L50:
	lw t0, -4(sp)
	lw t0, -4(t0)
	addi t0, t0, -24
	lw t1, 0(t0)
	lw t0, -4(sp)
	lw t0, -4(t0)
	lw t0, -12(sp)
	lw t0, 0(t0)
	lw t2, 0(t0)
	mul t1, t1, t2
	lw t0, -4(sp)
	lw t0, -4(t0)
	addi t0, t0, -28
	sw t1, 0(t0)
L51:
	lw t0, -4(sp)
	lw t0, -4(t0)
	lw t0, -16(sp)
	lw t0, 0(t0)
	lw t1, 0(t0)
	lw t0, -4(sp)
	lw t0, -4(t0)
	addi t0, t0, -28
	lw t2, 0(t0)
	beq t1, t2, L52
L52:
	j L54
L53:
	lw t0, -8(sp)
	li t1, 1
	sw t1, 0(t0)
	lw ra, (sp)
	addi sp, sp, 32
	jr ra
L54:
	j L55
L55:
	lw t0, -8(sp)
	li t1, 0
	sw t1, 0(t0)
	lw ra, (sp)
	addi sp, sp, 32
	jr ra
L56:
	li a0, 0
	li a7, 10
	ecall
L57:
	sw ra, 0(sp)
L58:
	lw t1, -12(sp)
	li t2, 1
	add t1, t1, t2
	lw t0, -4(sp)
	addi t0, t0, -20
	sw t1, 0(t0)
L59:
	lw t0, -4(sp)
	addi t0, t0, -20
	lw t1, 0(t0)
	sw t1, -12(sp)
L60:
	li t1, 2
	lw t0, -4(sp)
	addi t0, t0, -16
	sw t1, 0(t0)
L61:
	lw t0, -4(sp)
	addi t0, t0, -16
	lw t1, 0(t0)
	lw t0, -4(sp)
	lw t0, -12(sp)
	lw t0, 0(t0)
	lw t2, 0(t0)
	blt t1, t2, L64
L62:
	j L75
L63:
	j L61
L64:
L65:
L66:
L67:
	addi fp, sp, 32
	lw t0, -4(sp)
	addi t0, t0, -16
	lw t0, 0(t0)
	sw t0, -12(fp)
L68:
	lw t0, -4(sp)
	lw t0, -12(sp)
	lw t0, 0(t0)
	lw t0, 0(t0)
	sw t0, -16(fp)
L69:
	addi t0, sp, -24
	sw t0, -8(fp)
L70:
	sw sp, -4(sp)
	addi sp, sp, -32
	jal divides
	addi sp, sp, 32
	addi sp, sp, -32
	jal L45
L71:
L72:
	lw t0, -4(sp)
	addi t0, t0, -32
	li t2, 1
	beq t1, t2, L70
L73:
	j L72
L74:
	lw t0, -8(sp)
	li t1, 0
	sw t1, 0(t0)
	lw ra, (sp)
	addi sp, sp, 32
	jr ra
L75:
	j L_
L76:
	lw t0, -4(sp)
	addi t0, t0, -16
	lw t1, 0(t0)
	li t2, 1
	add t1, t1, t2
	lw t0, -4(sp)
	addi t0, t0, -28
	sw t1, 0(t0)
L77:
	lw t0, -4(sp)
	addi t0, t0, -28
	lw t1, 0(t0)
	lw t0, -4(sp)
	addi t0, t0, -16
	sw t1, 0(t0)
L78:
	j L61
L79:
	lw t0, -8(sp)
	li t1, 1
	sw t1, 0(t0)
	lw ra, (sp)
	addi sp, sp, 32
	jr ra
L80:
	li a0, 0
	li a7, 10
	ecall
L81:
	sw ra, 0(sp)
L82:
	lw t1, -12(sp)
	li t2, 1
	add t1, t1, t2
	lw t0, -4(sp)
	lw t0, -4(t0)
	addi t0, t0, -16
	sw t1, 0(t0)
L83:
	lw t0, -4(sp)
	lw t0, -4(t0)
	addi t0, t0, -16
	lw t1, 0(t0)
	sw t1, -12(sp)
L84:
	lw t0, -4(sp)
	lw t0, -4(t0)
	lw t0, -12(sp)
	lw t0, 0(t0)
	lw t1, 0(t0)
	lw t0, -4(sp)
	lw t0, -4(t0)
	lw t0, -12(sp)
	lw t0, 0(t0)
	lw t2, 0(t0)
	mul t1, t1, t2
	lw t0, -4(sp)
	lw t0, -4(t0)
	addi t0, t0, -20
	sw t1, 0(t0)
L85:
	lw t0, -8(sp)
	lw t0, -4(sp)
	lw t0, -4(t0)
	addi t0, t0, -20
	lw t1, 0(t0)
	sw t1, 0(t0)
	lw ra, (sp)
	addi sp, sp, 24
	jr ra
L86:
	li a0, 0
	li a7, 10
	ecall
L87:
	sw ra, 0(sp)
L88:
	lw t1, -12(sp)
	li t2, 1
	add t1, t1, t2
	lw t0, -4(sp)
	addi t0, t0, -20
	sw t1, 0(t0)
L89:
	lw t0, -4(sp)
	addi t0, t0, -20
	lw t1, 0(t0)
	sw t1, -12(sp)
L90:
L91:
L92:
	addi fp, sp, 24
	lw t0, -4(sp)
	lw t0, -12(sp)
	lw t0, 0(t0)
	lw t0, 0(t0)
	sw t0, -12(fp)
L93:
	addi t0, sp, -24
	sw t0, -8(fp)
L94:
	sw sp, -4(sp)
	addi sp, sp, -24
	jal sqr
	addi sp, sp, 24
	addi sp, sp, -24
	jal L79
L95:
L96:
L97:
L98:
	addi fp, sp, 24
	lw t0, -4(sp)
	lw t0, -12(sp)
	lw t0, 0(t0)
	lw t0, 0(t0)
	sw t0, -12(fp)
L99:
	addi t0, sp, -28
	sw t0, -8(fp)
L100:
	sw sp, -4(sp)
	addi sp, sp, -24
	jal sqr
	addi sp, sp, 24
	addi sp, sp, -24
	jal L79
L101:
L102:
	lw t0, -4(sp)
	addi t0, t0, -24
	lw t0, -4(sp)
	addi t0, t0, -24
	mul t1, t1, t2
	lw t0, -4(sp)
	addi t0, t0, -32
	sw t1, 0(t0)
L103:
	lw t0, -4(sp)
	addi t0, t0, -32
	lw t1, 0(t0)
	lw t0, -4(sp)
	addi t0, t0, -16
	sw t1, 0(t0)
L104:
	lw t0, -8(sp)
	lw t0, -4(sp)
	addi t0, t0, -16
	lw t1, 0(t0)
	sw t1, 0(t0)
	lw ra, (sp)
	addi sp, sp, 36
	jr ra
L105:
	li a0, 0
	li a7, 10
	ecall
L106:
	sw ra, 0(sp)
L107:
	lw t1, -12(sp)
	li t2, 1
	add t1, t1, t2
	lw t0, -4(sp)
	addi t0, t0, -16
	sw t1, 0(t0)
L108:
	lw t0, -4(sp)
	addi t0, t0, -16
	lw t1, 0(t0)
	sw t1, -12(sp)
L109:
	lw t0, -4(sp)
	lw t0, -12(sp)
	lw t0, 0(t0)
	lw t1, 0(t0)
	li t2, 4
	rem t1, t1, t2
	lw t0, -4(sp)
	addi t0, t0, -20
	sw t1, 0(t0)
L110:
	lw t0, -4(sp)
	addi t0, t0, -20
	lw t1, 0(t0)
	li t2, 0
	beq t1, t2, L107
L111:
	j L110
L112:
	lw t0, -4(sp)
	lw t0, -12(sp)
	lw t0, 0(t0)
	lw t1, 0(t0)
	li t2, 100
	rem t1, t1, t2
	lw t0, -4(sp)
	addi t0, t0, -24
	sw t1, 0(t0)
L113:
	lw t0, -4(sp)
	addi t0, t0, -24
	lw t1, 0(t0)
	li t2, 0
	bne t1, t2, L113
L114:
	j L110
L115:
	lw t0, -4(sp)
	lw t0, -12(sp)
	lw t0, 0(t0)
	lw t1, 0(t0)
	li t2, 400
	rem t1, t1, t2
	lw t0, -4(sp)
	addi t0, t0, -28
	sw t1, 0(t0)
L116:
	lw t0, -4(sp)
	addi t0, t0, -28
	lw t1, 0(t0)
	li t2, 0
	beq t1, t2, L113
L117:
	j L115
L118:
	lw t0, -8(sp)
	li t1, 1
	sw t1, 0(t0)
	lw ra, (sp)
	addi sp, sp, 32
	jr ra
L119:
	j L116
L120:
	lw t0, -8(sp)
	li t1, 0
	sw t1, 0(t0)
	lw ra, (sp)
	addi sp, sp, 32
	jr ra
L121:
	li a0, 0
	li a7, 10
	ecall
Lmain:
	addi sp, sp, -2
	mv fp, sp
L122:
	li t1, 0
	sw t1, -12(sp)
L123:
	li a7, 5
	ecall
	lw t0, -4(sp)
	addi t0, t0, -12
	sw a0, 0(t0)
L124:
	lw t0, -4(sp)
	addi t0, t0, -12
	lw a0, 0(t0)
	li a7, 1
	ecall
	la a0, str_nl
	li a7, 4
	ecall
L125:
	li t1, 1600
	lw t0, -4(sp)
	addi t0, t0, -12
	sw t1, 0(t0)
L126:
	lw t0, -4(sp)
	addi t0, t0, -12
	lw t1, 0(t0)
	li t2, 2000
	ble t1, t2, L126
L127:
	j L133
L128:
	j L123
L129:
L130:
L131:
	addi fp, sp, 32
	lw t0, -4(sp)
	addi t0, t0, -12
	lw t0, 0(t0)
	sw t0, -12(fp)
L132:
	addi t0, sp, -16
	sw t0, -8(fp)
L133:
	sw sp, -4(sp)
	addi sp, sp, -32
	jal leap
	addi sp, sp, 32
	addi sp, sp, -32
	jal L101
L134:
L135:
	li a7, 1
	ecall
	la a0, str_nl
	li a7, 4
	ecall
L136:
	lw t0, -4(sp)
	addi t0, t0, -12
	lw t1, 0(t0)
	li t2, 400
	add t1, t1, t2
	lw t0, -4(sp)
	addi t0, t0, -20
	sw t1, 0(t0)
L137:
	lw t0, -4(sp)
	addi t0, t0, -20
	lw t1, 0(t0)
	lw t0, -4(sp)
	addi t0, t0, -12
	sw t1, 0(t0)
L138:
	j L123
L139:
L140:
L141:
	addi fp, sp, 32
	li t0, 2023
	sw t0, -12(fp)
L142:
	addi t0, sp, -24
	sw t0, -8(fp)
L143:
	sw sp, -4(sp)
	addi sp, sp, -32
	jal leap
	addi sp, sp, 32
	addi sp, sp, -32
	jal L101
L144:
L145:
	li a7, 1
	ecall
	la a0, str_nl
	li a7, 4
	ecall
L146:
L147:
L148:
	addi fp, sp, 32
	li t0, 2024
	sw t0, -12(fp)
L149:
	addi t0, sp, -28
	sw t0, -8(fp)
L150:
	sw sp, -4(sp)
	addi sp, sp, -32
	jal leap
	addi sp, sp, 32
	addi sp, sp, -32
	jal L101
L151:
L152:
	li a7, 1
	ecall
	la a0, str_nl
	li a7, 4
	ecall
L153:
L154:
L155:
	addi fp, sp, 36
	li t0, 3
	sw t0, -12(fp)
L156:
	addi t0, sp, -32
	sw t0, -8(fp)
L157:
	sw sp, -4(sp)
	addi sp, sp, -36
	jal quad
	addi sp, sp, 36
	addi sp, sp, -36
	jal L86
L158:
L159:
	li a7, 1
	ecall
	la a0, str_nl
	li a7, 4
	ecall
L160:
L161:
L162:
	addi fp, sp, 40
	li t0, 5
	sw t0, -12(fp)
L163:
	addi t0, sp, -36
	sw t0, -8(fp)
L164:
	sw sp, -4(sp)
	addi sp, sp, -40
	jal fib
	addi sp, sp, 40
	addi sp, sp, -40
	jal L20
L165:
L166:
	li a7, 1
	ecall
	la a0, str_nl
	li a7, 4
	ecall
L167:
	li t1, 1
	lw t0, -4(sp)
	addi t0, t0, -12
	sw t1, 0(t0)
L168:
	lw t0, -4(sp)
	addi t0, t0, -12
	lw t1, 0(t0)
	li t2, 12
	ble t1, t2, L153
L169:
	j L160
L170:
	j L150
L171:
L172:
L173:
	addi fp, sp, 32
	lw t0, -4(sp)
	addi t0, t0, -12
	lw t0, 0(t0)
	sw t0, -12(fp)
L174:
	addi t0, sp, -40
	sw t0, -8(fp)
L175:
	sw sp, -4(sp)
	addi sp, sp, -32
	jal isPrime
	addi sp, sp, 32
	addi sp, sp, -32
	jal L57
L176:
L177:
	li a7, 1
	ecall
	la a0, str_nl
	li a7, 4
	ecall
L178:
	lw t0, -4(sp)
	addi t0, t0, -12
	lw t1, 0(t0)
	li t2, 1
	add t1, t1, t2
	lw t0, -4(sp)
	addi t0, t0, -44
	sw t1, 0(t0)
L179:
	lw t0, -4(sp)
	addi t0, t0, -44
	lw t1, 0(t0)
	lw t0, -4(sp)
	addi t0, t0, -12
	sw t1, 0(t0)
L180:
	j L150
L181:
	lw a0, -12(sp)
	li a7, 1
	ecall
	la a0, str_nl
	li a7, 4
	ecall
L182:
	li a0, 0
	li a7, 10
	ecall
