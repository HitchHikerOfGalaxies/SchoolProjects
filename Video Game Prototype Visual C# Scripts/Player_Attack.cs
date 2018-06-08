using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class Player_Attack : MonoBehaviour
{
    private bool attacking = false;
    private bool proattacking = false;

    private float attackTimer = 0;
    private float attackCd = 0.3f;
    public int Exp = 0;
    [SerializeField] int Level = 1;
    public int SkillTree = 0;

    public Collider2D attackTrigger;

    private Animator anim;

    // Use this for initialization
    
    void Awake()
    {
        anim = gameObject.GetComponent<Animator>();
        attackTrigger.enabled = false;

    }

    // Update is called once per frame
    void Update()
    {
        Exp = ExpManager.instance.curExp;
        if (Exp == 4)
        {
            Level += Exp;
            Exp = 0;
        }
        if (Level >= 4)
        {
            SkillTree = 1;
            Level = 4;
        }
            if (Input.GetButtonDown("Fire1"))
        {

            attacking = true;
            attackTimer = attackCd;

            attackTrigger.enabled = true;
        }
        if (attacking)
        {
            if (attackTimer > 0)
            {
                attackTimer -= Time.deltaTime;
            }
            else
            {
                attacking = false;
                attackTrigger.enabled = false;
            }
            anim.SetBool("Attacking", attacking);
        }
        if (Input.GetKeyDown(KeyCode.F) && Level >= 4)
        {

            proattacking = true;
            attackTimer = attackCd;

            attackTrigger.enabled = true;
        }
        if (proattacking)
        {
            if (attackTimer > 0)
            {
                attackTimer -= Time.deltaTime;
            }
            else
            {
                proattacking = false;
                attackTrigger.enabled = false;
            }
            anim.SetBool("ProAttacking", proattacking);
        }
    }

}
