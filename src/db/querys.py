#QUERYS ALTO VALOR

def insert_notif(canal,msisdn,fr,id_event,monto):
    return f"""INSERT INTO public.notificaciones
            (canal, msisdn, fecha_registro, id_evento_id, monto)
            VALUES('{canal}', '{msisdn}', '{fr}', {id_event}, {monto});"""

#QUERYS SCE PROYECTOS

def insert_tbl(msisdn, ini_fec,ini_estado,now_fec,now_estado,now_monto):
    return f""" INSERT INTO sce_proyectos.tbl_altovalor_estado
            (msisdn, ini_fec, ini_estado, now_fec, now_estado, now_monto)
            VALUES('{msisdn}', '{ini_fec}', {ini_estado}, '{now_fec}', {now_estado}, {now_monto}); """


def delete_tbl(id):
    return f""" DELETE FROM sce_proyectos.tbl_altovalor_estado
            WHERE id='{id}'; """

def select_tbl(msisdn):
    return f""" SELECT id, msisdn, ini_fec, ini_estado, now_fec, now_estado, now_monto
            FROM sce_proyectos.tbl_altovalor_estado 
            where msisdn='{msisdn}'; """