﻿using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class attackTrigger : MonoBehaviour {
    
    public int dmg;

    void OnTriggerEnter2D(Collider2D col)
    {
        if (col.isTrigger != true && col.CompareTag("enemy"))
        {
            col.SendMessageUpwards("Damage", dmg);
            col.SendMessageUpwards("Hitstun", dmg);
        }
    }
}
